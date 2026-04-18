import unittest

class TestApp(unittest.TestCase):
    def test_basic_math(self):
        # A simple test to prove the testing framework runs
        self.assertEqual(1 + 1, 2)
        
    def test_imports(self):
        # Proves the app can import standard libraries
        import os
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()