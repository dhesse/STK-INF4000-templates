import numpy as np
from operator import add

def delta(x1, x2):
    """Distance metric between two n-dimensional points, for arbitrary
    n. Obeys the standard definitions

    d(x, y) >= 0 for all x, y
    d(x, x) = 0 for all x
    d(x, y) = d(y, x)
    d(x, z) <= d(x, y) + d(y, z)

    """
    return np.sqrt(np.sum((x1-x2)**2))

def value_normalizer(RDD):
    """Given an RDD containing records of the form [k, (X1, X2, ...)],
    returns a transformed RDD such that all the Xi have zero mean and
    unit variance.

    Assumes that each value of the RDD is a numpy array.

    Example:
    
    >>> data = sc.parallelize([(1, np.array([1.0])), 
    ...            (2, np.array([2.0])), (3, np.array([3.0]))])
    >>> value_normalizer(data).collect()
    [(1, array([-1.22474487])),
     (2, array([ 0.])),
     (3, array([ 1.22474487]))]
    """
    N = RDD.count()
    mu = RDD.map(lambda (_, v): v).reduce(add) / N
    sigma = np.sqrt(RDD.map(lambda (_, x): (x - mu)**2).reduce(add) / N)
    return RDD.map(lambda (k, x): (k, (x - mu) / sigma))

def KNN(k, RDD, x, metric=delta):
    """Given an RDD containing records of the form [l, y],
    an integer k and a point x, finds the k closest y to x in the RDD
    according the metric passed as argument and returns the average
    value for l of those."""
    k_nearest = (RDD
                 .map(lambda (l, y): (l, metric(x, y)))
                 .takeOrdered(k, lambda (l, dist): dist))
    return np.mean([l for l, dist in n_nearest])
