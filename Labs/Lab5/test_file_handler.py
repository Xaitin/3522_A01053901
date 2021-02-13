from unittest import TestCase
from file_handler import file_handler


class Testfile_handler(TestCase):
    def test_write_lines(self):
        file_handler.write_lines("testing.txt", "Testing")
        myfile = open("testing.txt", "r")
        lines = myfile.readlines()
        myfile.close()
        self.assertTrue("Testing" in lines[-1])
