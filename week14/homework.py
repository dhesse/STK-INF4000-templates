def bigrams_excluding(text, stopwords):
    """Extract bigrams from text, returning only those that don't
    incude words occuring in stopwords.

    Example:
    >>> text = "after all is said and done".split()
    >>> stopwords = set(['and'])
    >>> list(homework.bigrams_excluding(text, stopwords))
    [('after', 'all'), ('all', 'is'), ('is', 'said')]
    """
    pass

def most_common_bigrams_excluding(corpus, stopwords, n):
    """Given a corpus of text and a number of stopwords, return the n
    most common bigrams not containing the given stopwords and their
    counts.

    Example:
    >>> corpus = ["after all is said and done".split(),
    ... "he got it after all".split()]
    >>> stopwords = set(['and'])
    >>> homework.most_common_bigrams_excluding(corpus, stopwords, 2)
    [(('after', 'all'), 2), (('all', 'is'), 1)]
    """
    pass

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
    pass

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
                                            BernoulliNB(), 100)
    """
    pass
