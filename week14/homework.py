from nltk import bigrams as nl_bigrams
from nltk.probability import FreqDist
from itertools import chain, ifilter
import pandas as pd

def bigrams_excluding(text, stopwords):
    """Extract bigrams from text, returning only those that don't
    incude words occuring stopwords.

    Example:
    >>> text = "after all is said and done".split()
    >>> stopwords = set(['and'])
    >>> list(homework.bigrams_excluding(text, stopwords))
    [('after', 'all'), ('all', 'is'), ('is', 'said')]
    """
    return ifilter(lambda (w1, w2): w1 not in stopwords and w2 not in
                   stopwords,
                   nl_bigrams(text))

def most_common_bigrams_excluding(corpus, stopwords, n):
    """Given a corpus of text and a number of stopwords, return the n
    mnost common bigrams not containing the given stopwords and their
    counts.

    Example:
    >>> corpus = ["after all is said and done".split(),
    ... "he got it after all".split()]
    >>> stopwords = set(['and'])
    >>> homework.most_common_bigrams_excluding(corpus, stopwords, 2)
    [(('after', 'all'), 2), (('all', 'is'), 1)]
    """
    return FreqDist(chain(*[bigrams_excluding(text, stopwords) for
                            text in corpus])).most_common(n)

def make_bigram_df(corpus, bigrams):
    """Given a corpus of text, make a pandas data frame that contains
    binary columns indicating presence of a set of bigrams in each of
    the corpus' texts.

    Example:
    >>> corpus = ["after all is said and done".split(),
    ... "he got it after all".split()]
    >>> bigrams = [('after', 'all'), ('said', 'and')]
    >>> homework.make_bigram_df(corpus, bigrams)
      after   said
        all    and
    0  True   True
    1  True  False
    """
    corpus_bigrams = [set(nl_bigrams(t)) for t in corpus]
    return pd.DataFrame({bigram: [bigram in text_bigram for
                                  text_bigram in corpus_bigrams]
                         for bigram in bigrams})

def make_bigram_classifier(pos_corpus, neg_corpus, base_classifier, n_bigrams):
    """Given a corpus of positive and negatve texts, make a classifier
    that will predict positive or negative sentiment in a text. Return
    the classifier and the relevant bigrams.

    >>> pos_dir = 'data/review_polarity/txt_sentoken/pos/'
    >>> positive = [open(pos_dir + text_file).read().split()
    ...              for text_file in os.listdir(pos_dir)]
    >>> neg_dir = 'data/review_polarity/txt_sentoken/neg/'
    >>> positive = [open(neg_dir + text_file).read().split()
    ...              for text_file in os.listdir(neg_dir)]
    from sklearn.naive_bayes import GaussianNB
    model, bigrams = make_bigram_classifier(positive[:800],
                                            negative[:800],
                                            GaussianNB(), 100)
    """
    from nltk.corpus import stopwords
    en_stop = set(stopwords.words('english'))
    en_stop.update(set(',."();:?-!'))
    bigrams = most_common_bigrams_excluding(chain(pos_corpus,
                                                  neg_corpus),
                                            en_stop,
                                            n_bigrams)
    bigrams = [b for b, c in bigrams]
    pos_df = make_bigram_df(pos_corpus, bigrams)
    neg_df = make_bigram_df(neg_corpus, bigrams)
    pos_df['sentiment'] = 1
    neg_df['sentiment'] = 0
    full_df = pos_df.append(neg_df)
    return base_classifier.fit(full_df[bigrams], full_df['sentiment']), bigrams
