import unittest
from homework import domain_name, process_tweet, get_most_common_domains
from collections import Iterable
import copy

class TestDomainName(unittest.TestCase):
    def test_no_pathl_http(self):
        """Basic example with HTTP protocol."""
        self.assertEqual(domain_name('http://subdomain.example.com'),
                         'subdomain.example.com')
    def test_no_path_https(self):
        """Basic example with HTTPS protocol."""
        self.assertEqual(domain_name('https://subdomain.example.com'),
                         'subdomain.example.com')
    def test_url_with_path(self):
        """Example with a path."""
        self.assertEqual(domain_name('http://subdomain.example.com/path/to/page'),
                         'subdomain.example.com')
        

class TestProcessTweet(unittest.TestCase):
    """Tests for the process_tweet function."""
    def setUp(self):
        """This will be called before every test run.
        
        After the call, the basic_tweet field will contain an entities
        key with some basic required structures.
        """
        self.basic_tweet = {'entities' : {'urls': []}}
        
    def test_should_return_iterable(self):
        """Result of process_tweet should be iterable, i.e. a list,
        tuple, generator, or similar."""
        self.assertIsInstance(process_tweet(self.basic_tweet),
                              Iterable)
    def test_should_return_empty_iter_with_empty_arg(self):
        """Called with no URLS, the result should be empty."""
        self.assertEqual(len(process_tweet(self.basic_tweet)), 0)
    def test_should_return_passed_urls(self):
        """Adding some URLS, whose domain names should be returned."""
        urls = self.basic_tweet['entities']['urls']
        urls.append({'expanded_url':
                     'http://www.example1.com/path/1'})
        urls.append({'expanded_url':
                     'http://www.example2.com/path/2'})
        self.assertItemsEqual(['www.example1.com',
                               'www.example2.com'],
                              process_tweet(self.basic_tweet))

class TestGetMostComonDomains(unittest.TestCase):
    """Tests for the get_most_common_domains function."""
    def setUp(self):
        """This will be called before every test run.
        
        After the call, the basic_tweet field will contain an entities
        key with some basic required structures.
        """
        self.basic_tweet = {'entities' : {'urls': []}}
    def test_should_return_iterable(self):
        """Result should be iterable, i.e. a list, tuple, generator,
        or similar."""
        self.assertIsInstance(get_most_common_domains([self.basic_tweet]),
                              Iterable)
    def test_empty_returns_empty_iterator(self):
        """Called with no tweets, should return empty iterator."""
        self.assertEqual(len(get_most_common_domains([])), 0)
    def test_one_tweet_one_domain(self):
        """Test with one tweet and one domain."""
        urls = self.basic_tweet['entities']['urls']
        urls.append({'expanded_url': 
                     'http://www.example1.com/path/1'})
        self.assertEqual(get_most_common_domains([self.basic_tweet]),
                         [('www.example1.com', 1)])
    def test_with_known_values(self):
        """Simple test with know values."""
        urls = ['http://www.example1.com/path/1',
                'http://www.example2.com/path/2',
                'http://www.example3.com/path/3',
                'http://www.example4.com/path/4']
        tweets = [copy.deepcopy(self.basic_tweet) for _ in range(len(urls))]
        for n, url, tweet in zip(range(len(urls)), urls, tweets):
            for i in range(n + 1):
                tweet['entities']['urls'].append({'expanded_url': url})
        result = get_most_common_domains(tweets)
        known = [('www.example{}.com'.format(i), i) for i in
                 (1,2,3,4)]
        self.assertItemsEqual(result, known)
    def test_should_not_return_more_than_n(self):
        """Make sure the n argument is obeyed."""
        urls = ['http://www.example1.com/path/1',
                'http://www.example2.com/path/2',
                'http://www.example3.com/path/3',
                'http://www.example4.com/path/4']
        tweets = [copy.deepcopy(self.basic_tweet) for _ in range(len(urls))]
        for n, url, tweet in zip(range(len(urls)), urls, tweets):
            for i in range(n + 1):
                tweet['entities']['urls'].append({'expanded_url': url})
        result = get_most_common_domains(tweets, 2)
        known = [('www.example{}.com'.format(i), i) for i in
                 (3,4)]
        self.assertItemsEqual(result, known)
        
