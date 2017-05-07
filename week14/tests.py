import unittest
import homework
from pandas import DataFrame
from pandas.util.testing import assert_frame_equal

class TestBigramsExcluding(unittest.TestCase):
    def test_known_values(self):
        text = "after all is said and done".split()
        stopwords = set(['and'])
        self.assertSequenceEqual(
            list(homework.bigrams_excluding(text, stopwords)),
            [('after', 'all'), ('all', 'is'), ('is', 'said')])

class TestMostCommonBigrams(unittest.TestCase):
    def test_known_values(self):
        corpus = ["after all is said and done".split(),
                  "he got it after all".split()]
        stopwords = set(['and'])
        self.assertEqual(
            homework.most_common_bigrams_excluding(corpus, stopwords, 2),
            [(('after', 'all'), 2), (('all', 'is'), 1)])

class TestMakeBigramDf(unittest.TestCase):
    def test_known_values(self):
        corpus = ["after all is said and done".split(),
                  "he got it after all".split()]
        bigrams = [('after', 'all'), ('said', 'and')]
        assert_frame_equal(
            homework.make_bigram_df(corpus, bigrams),
            DataFrame({('after', 'all'): [True, True],
                       ('said', 'and'): [True, False]}))

if __name__ == '__main__':
    unittest.main()

