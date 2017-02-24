def delta(x1, x2):
    """Distance metric between two n-dimensional points, for arbitrary
    n. Obeys the standard definitions

    d(x, y) >= 0 for all x, y
    d(x, x) = 0 for all x
    d(x, y) = d(y, x)
    d(x, z) <= d(x, y) + d(y, z)

    """
    pass

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
    pass

def KNN(k, RDD, x, metric=delta):
    """Given an RDD containing records of the form [l, y],
    an integer k and a point x, finds the k closest y to x in the RDD
    according the metric passed as argument and returns the average
    value for l of those."""
    pass
