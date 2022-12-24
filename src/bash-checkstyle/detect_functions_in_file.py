# Include trivial function to test helper_file_edit.
from src.helper_file_edit import read_file
from src.helper_text_parsing import get_function_line_nrs


def add_two(x):
    return x + 2


def get_functions_in_file(filepath, rules):
    """Returns a list of bash function objects consisting of the comments and
    bash code that are found in a file.

    :param filepath: The path to the bash file that is read.
    """
    # Get Bash file content.
    filecontent = read_file(filepath)

    # Get start and end line nrs of functions.
    function_starts = get_function_line_nrs(filecontent, rules)

    # Get start and end line nrs of function comments.

    # Convert bash code and comments into function object.
    functions = [function_starts]
    return functions
