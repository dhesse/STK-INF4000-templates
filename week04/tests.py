import unittest
import pandas as pd
import numpy as np
from io import StringIO

from homework import read_file_or_buffer, add_squared_column, transform, MSE, MSE_KNN

class TestReadFileOrBuffer(unittest.TestCase):
    def test_known_values(self):
        """Test with a simple example."""
        file_contents = u"A,B\n1,2\n3,4\n"
        string_io = StringIO(file_contents)
        known = pd.DataFrame({'A': [1,3], 'B': [2,4]})
        result = read_file_or_buffer(string_io)
        pd.util.testing.assert_frame_equal(known, result)
        self.assertIsInstance(result, pd.DataFrame,
                              "Should return DataFrame")
    def test_alternative_delimiter(self):
        """Test with '|' as delimiter."""
        file_contents = u"A|B\n1|2\n3|4\n"
        string_io = StringIO(file_contents)
        known = pd.DataFrame({'A': [1,3], 'B': [2,4]})
        result = read_file_or_buffer(string_io, '|')
        self.assertTrue(all(result == known))
        self.assertIsInstance(result, pd.DataFrame)

class TestAddSquaredRow(unittest.TestCase):
    def test_known_values(self):
        """Simple known values test."""
        a = pd.DataFrame({'A': [1,2,3]})
        add_squared_column(a, 'A')
        known = pd.DataFrame({'A': [1,2,3],
                              'A_sq': [1,4,9]})
        pd.util.testing.assert_frame_equal(a, known)

class TestTransform(unittest.TestCase):
    def test_known_values(self):
        a = pd.DataFrame({'A': [1,2,3],
                          'B': [0.1, 0.2, 0.3]})
        f = lambda x, y: x + y
        transform(a, 'C', f, 'A', 'B')
        known = pd.DataFrame({'A': [1,2,3],
                              'B': [0.1, 0.2, 0.3],
                              'C': [1.1, 2.2, 3.3]})
        pd.util.testing.assert_frame_equal(a, known)

class TestMSE(unittest.TestCase):
    def test_known_values(self):
        y = np.random.standard_normal(20)
        yp = np.random.standard_normal(20)
        np.testing.assert_almost_equal(
            MSE(y, yp), np.mean((y-yp)**2))

class TestMSE_KNN(unittest.TestCase):
    def test_with_training(self):
        x = [[i] for i in np.random.standard_normal(20)]
        y = np.random.standard_normal(20)
        self.assertAlmostEqual(0, MSE_KNN(x,y,x,y,1))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
