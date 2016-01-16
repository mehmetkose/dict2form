import unittest
from dict2form import dict2form

my_dict = {'unit': 'tests'}

my_dict_with_sub_dict = {'lorem': 'ipsum', 'sit': {'dolor': 'amet'}}

my_dict_with_sub_list = {'lorem': 'ipsum', 'sit': ['dolor', 'amet']}

class TestStringMethods(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(dict2form(my_dict), str)

    def test_in_form(self):
        self.assertIn("<form", dict2form(my_dict))

    def test_submit(self):
        self.assertIn("submit", dict2form(my_dict))

    def test_sub_dict(self):
        self.assertIn("dolor", dict2form(my_dict_with_sub_dict))

    def test_sub_list(self):
    	print(my_dict_with_sub_list)
        self.assertIn("dolor", dict2form(my_dict_with_sub_list))


if __name__ == '__main__':
    unittest.main()
