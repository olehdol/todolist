import todo   # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(todo.increment(3), 4)

    def test_decrement(self):
        self.assertEqual(todo.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()
