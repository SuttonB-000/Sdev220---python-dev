''' contains first test case'''

# what to test and is it a unit test or an integration test
# test workflow 
#   {create inputs} --> {execute code being tested, capture output} --> {compare output and expected result}
#   for sum.py tut --> can it sum ints? can it sum tuple or set? can it sum floats? Bad value? A negative?

import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    # whole num or integer test
    def test_list_int(self):
        #test method
        data = [ 1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

# tuple test
class TestTupleSum(unittest.TestCase):
    def test_tuple(self):
        data = ( 1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)

class TestFloatSum(unittest.TestCase):
    def test_float(self):
        data = ( 4, 2, 2)
        result = sum(data)
        self.assertEqual(result, 8)

class TestNegative(unittest.TestCase):
    def test_negs(self):
        data = [ 1, -1, 0]
        result = sum(data)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
