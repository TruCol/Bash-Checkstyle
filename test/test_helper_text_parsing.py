import unittest
import os

from src.__main__ import add_two
from src.helper_file_edit import read_file
from src.helper_text_parsing import get_function_line_nrs
from src.rules import Rules


class Test_function_detection(unittest.TestCase):

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_function_detection, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.rules = Rules()

    # Returns the directory of this script regardles of from which level the
    # code is executed.
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # Tests unit test on add_two function of main class.
    def test_add_two(self):

        expected_result = 7
        result = add_two(5)
        self.assertEqual(expected_result, result)

    def test_get_function_line_nrs(self):

        expected_result = [25, 50], [32, 66]

        # Get Bash file content.
        filecontent = read_file("test/example_files/2_functions.sh")
        result = get_function_line_nrs(filecontent, self.rules)
        self.assertEqual(expected_result, result)
