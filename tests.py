import unittest
from dict2form import dict2form

myDict = {'unit':'tests'}

myDictWithSub = {'lorem':'ipsum', 'sit':{'dolor':'amet'}}


class TestStringMethods(unittest.TestCase):


    def test_type(self):
        self.assertIsInstance(dict2form(myDict), str)

    def test_in_form(self):
        self.assertIn("<form", dict2form(myDict))

    def test_submit(self):
        self.assertIn("submit", dict2form(myDict))

    def test_sub_dict(self):
        self.assertIn("dolor", dict2form(myDictWithSub))


if __name__ == '__main__':
    unittest.main()
