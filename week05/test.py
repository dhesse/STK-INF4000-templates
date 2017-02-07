from homework import return_unique, fib, safe_call, curve_predict
import unittest
import numpy as np

class TestReturnUnique(unittest.TestCase):
    def test_ru(self):
        self.assertItemsEqual('abcd',
                              return_unique('aabcbdacd'))

class TestFib(unittest.TestCase):
    def test_fib(self):
        known = [1, 5]
        for i in range(2, 50):
            self.assertItemsEqual(known,
                                  fib(i, known[0], known[1]))
            known.append(known[-1] + known[-2])

class TestSafeCall(unittest.TestCase):
    def test_no_throw(self):
        self.assertEqual(5,
                         safe_call(lambda : 5))
    def test_catches_value_error(self):
        def raise_value_error():
            raise ValueError()
        self.assertEqual(None, safe_call(raise_value_error))
    def test_raises_name_error(self):
        def raise_name_error():
            raise NameError()
        with self.assertRaises(NameError):
            safe_call(raise_name_error)

class TestCurePredict(unittest.TestCase):
    def test_known_values(self):
        def f(x, a, b, c):
            return a + b*x + c*x**2
        params = (4, 2.5, 0.5)
        xtrain = np.arange(0, 10, 0.2)
        ytrain = f(xtrain, *params)
        cp = curve_predict(f, xtrain, ytrain, xtrain)
        np.testing.assert_allclose(cp, ytrain)
    
if __name__ == '__main__':
    unittest.main()
