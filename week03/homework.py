def domain_name(url):
    """Return the domain name of a URL.

    Example:
    
    >>> domain_name('https://www.example.com/news/index.html')
    'www.example.com'
    """
    pass

def process_tweet(status):
    """Return the domain names of all URLS contained in a tweet.

    Example:
    >>> tweet = {'entities':
                   {'urls': [{'expanded_url': 
                                'http://www.example1.com/path/1'},
                             {'expanded_url':
                                'http://www.example2.com/path/2'}]}}
    >>> process_tweet(tweet)
    ['www.example1.com', 'www.example2.com']
    """  
    pass

def get_most_common_domains(statuses, n = 5):
    """Given a number of statuses, retrieve the n most commonly linked
    URLs.

    Example:
    >>> tweet = {'entities':
                   {'urls': [{'expanded_url': 
                                'http://www.example1.com/path/1'}]}}
    >>> get_most_common_domains([tweet])
    >>> [('www.example1.com', 1)]
    """
    pass
