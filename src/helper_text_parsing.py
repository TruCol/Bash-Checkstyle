# Include trivial funciton to test helper_file_edit.
import re


def add_two(x):
    return x + 2


def get_function_line_nrs(filecontent, rules):
    """Returns two lists containing the starting and ending line numbers of
    the functions respectively.

    :param filecontent: The content of the bash file that is being analysed.
    :param rules: The Bash formatting rules that are chosen by the user.
    """
    function_start_line_nrs = []
    function_end_line_nrs = []

    line_nr = 0
    for line in filecontent:
        line_nr += 1

        # Check if a function description as specified in the ruleset occurs.
        if re.search(rules.re_function_declaration_chars, line):
            print(f"line={line}")

            if len(function_start_line_nrs) != len(function_end_line_nrs):
                raise Exception("Error, function end is not found.")
            function_start_line_nrs.append(line_nr)

        if line[0] == rules.function_ending_char:
            function_end_line_nrs.append(line_nr)

            if len(function_start_line_nrs) != len(function_end_line_nrs):
                raise Exception("Error, function end is not found.")
    return function_start_line_nrs, function_end_line_nrs
