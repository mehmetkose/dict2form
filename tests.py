import unittest
from dict2form import dict2form

myDict = {'unit':'tests'}

class TestStringMethods(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(dict2form(myDict), str)

    def test_in_form(self):
        self.assertIn("<form", dict2form(myDict))

    def test_submit(self):
        self.assertIn("submit", dict2form(myDict))


if __name__ == '__main__':
    unittest.main()
