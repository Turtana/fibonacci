import fib
import unittest

class FibTests(unittest.TestCase):

    def test1(self):
        result = fib.fib(1, 5)
        self.assertEqual(result, [1, 1, 2, 3, 5])

    def test2(self):
        result = fib.fib(5, 10)
        self.assertEqual(result, [5, 8, 13, 21, 34, 55, 89, 144, 233, 377])

    def test3(self):
        result = fib.fib(100, 10)
        self.assertEqual(result, [144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946])

    def test4(self):
        result = fib.fib("duck", 6)
        self.assertEqual(result, -1)

    def test5(self):
        result = fib.fib(1, 6)
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 7]) # this should fail

if __name__ == '__main__':
    unittest.main()
