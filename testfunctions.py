import unittest

from formatdata import *
from generatedata import *
from getdata import *


class TestMethods(unittest.TestCase):
    # if you run this tests, generate new data in .txt, get and format new data
    # and you can see that everything is ok

    def test_generatedata(self):
        for i in range(len(textfiles[0])):
            self.assertEqual(80, populate_files(80, str(textfiles[0][i])))

    def test_getdata(self):
        self.assertEqual(len(numbers_from_odt) + len(numbers_from_txt), get_all_data())

    def test_formatdata(self):
        self.assertEqual(80 * (len(textfiles[0])), format_data())


if __name__ == "__main__":
    unittest.main()
