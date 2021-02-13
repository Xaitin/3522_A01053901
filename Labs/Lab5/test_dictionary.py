from unittest import TestCase
from dictionary import dictionary


class Testdictionary(TestCase):
    def test_load_dictionary(self):
        test_dict = dictionary()
        test_dict.load_dictionary("data.json")
        self.assertTrue(test_dict._is_loaded)

    def test_query_definition(self):
        test_dict = dictionary()
        test_dict.load_dictionary("data.json")
        my_test_var = test_dict.query_definition("abandon")
        self.assertTrue(type(my_test_var) == str)
