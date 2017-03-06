import unittest
import numpy as np
from homework import LDA
from pyspark import SparkContext

sc = SparkContext()

class SparkLDATest(unittest.TestCase):
    def test_known_values(self):
        mu = [[0, 0], [10, 10]]
        sigma = [[1, 0], [0, 1]]
        points = []
        labels = []
        N = 10000
        for i, m in enumerate(mu):
            points.append(np.random.multivariate_normal(m, sigma, N))
            labels += [i]*N
        points = np.vstack(points)
        RDD = sc.parallelize([(x, i) for x, i in zip(points, labels)])
        pis, Sigma, mus = LDA(RDD)
        self.assertEqual(sorted(pis.keys()), [0,1])
        self.assertEqual(sorted(mus.keys()), [0,1])
        atol = 0.1
        rtol = 0.1
        np.testing.assert_allclose(sigma, Sigma, atol=atol, rtol=rtol)
        for i in range(2):
            np.testing.assert_allclose(mu[i], mus[i], atol=atol, rtol=rtol)
            np.testing.assert_allclose(pis[i], 0.5, atol=atol,  rtol=rtol)

if __name__ == '__main__':
    unittest.main()
