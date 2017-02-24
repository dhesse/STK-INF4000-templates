import unittest
from homework import *
import numpy as np
import itertools
from operator import add
from pyspark import SparkContext

sc = SparkContext()

class TestDelta(unittest.TestCase):
    def test_bigger_zero(self):
        '''The distance between any two points should be bigger than
        zero.'''
        for dim in 2,3,4:
            points = [np.random.standard_normal(dim) for d in
                      range(20)]
            for x1, x2 in itertools.combinations(points, 2):
                self.assertGreaterEqual(delta(x1, x2), 0)
                self.assertEqual(delta(x1, x2), delta(x2, x1))
            for x in points:
                self.assertAlmostEqual(delta(x,x), 0)
    def test_triangle_inequality(self):
        '''Triangle inequality, d(x, z) <= d(x,y) + d(y,z).'''
        for dim in 2,3,4:
            points = [np.random.standard_normal(dim) for d in
                      range(20)]
            for x1, x2, x3 in itertools.combinations(points, 3):
                self.assertGreaterEqual(delta(x1, x2) + delta(x2, x3),
                                        delta(x1, x3))

class TestNormalizer(unittest.TestCase):
    def test_known_values(self):
        RDD = sc.parallelize([(1, np.random.uniform(-2, 2, 3)) for i in
                              range(100)])
        result = value_normalizer(RDD)
        mu = result.map(lambda (_, v): v).reduce(add) / 100
        np.testing.assert_array_almost_equal(mu, [0]*3)
        var = result.map(lambda (_, x): x**2).reduce(add) / 100
        np.testing.assert_array_almost_equal(var, [1]*3)


class TestKNN(unittest.TestCase):
    def test_known_values(self):
        RDD = sc.parallelize([(1, np.array([1,2,3]))]*3
                             + [(2, np.array([3,2,1]))]*3)
        self.assertAlmostEqual(KNN(3, RDD, np.array([1,2,3])), 1)
        self.assertAlmostEqual(KNN(3, RDD, np.array([3,2,1])), 2)
                             
if __name__ == '__main__':
    unittest.main()
