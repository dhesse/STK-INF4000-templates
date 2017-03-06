import numpy as np
from operator import add

def LDA(RDD):
    '''Given a Spark RDD consisting of pairs (x, g), where x is a
    numpy array and g is an integer label, return the priors pi, the
    variance-covariance matrix Sigma, and the group means mu for
    linear discriminant analysis.

    Returns: (pi, Sigma, mu)
             where pi, mu are dictionaries containing the priors and
             centers for each class.

    Example:
    >>> mu = [[0, 0], [10, 10]]
    >>> sigma = [[1, 0], [0, 1]]
    >>> points = []
    >>> labels = []
    >>> N = 10000
    >>> for i, m in enumerate(mu):
    ...     points.append(np.random.multivariate_normal(m, sigma, N))
    ...     labels += [i]*N
    ...
    >>> points = np.vstack(points)
    >>> RDD = sc.parallelize([(x, i) for x, i in zip(points, labels)])
    >>> pis, Sigma, mus = LDA(RDD)
    >>> mus
    {0: array([-0.02056332,  0.00299521]),
     1: array([  9.99377919,  10.01389058])}
    >>> pis
    {0: 0.5, 1: 0.5}
    >>> Sigma
    array([[ 1.0033927 ,  0.01500472],
       [ 0.01500472,  0.9900926 ]])
    '''
    N = RDD.count()
    Ns = RDD.map(lambda (_, g): (g, None)).countByKey()
    pis = {i: Ns[i]/float(N) for i in Ns}
    sums = RDD.map(lambda (x, g): (g, x)).reduceByKey(add).collect()
    mus = {l: s/Ns[l] for l,s in sums}
    Sigma = (RDD
             .map(lambda (x, l): np.dot((x-mus[l]).reshape(-1,1),
                                        (x-mus[l]).reshape(1,-1)))
             .reduce(add))
    Sigma /= float(N - len(Ns))
    
    return pis, Sigma, mus
