import os
import unittest

from src.__main__ import add_two
from src.rules import Rules


class Test_function_detection(unittest.TestCase):
    # Initialize test object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        self.rules = Rules()

    # Returns the directory of this script regardless of from which level the
    # code is executed.
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # Tests unit test on add_two function of main class.
    def test_add_two(self):
        expected_result = 7
        result = add_two(5)
        self.assertEqual(expected_result, result)
