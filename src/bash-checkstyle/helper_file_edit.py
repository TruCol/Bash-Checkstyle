# Include trivial function to test helper_file_edit.
def add_two(x):
    return x + 2


# Read file and return as list.
def read_file(filepath):
    try:
        with open(filepath) as file:
            lines = file.readlines()
        return lines
    except FileExistsError:
        raise Exception(f"Was not able to read file at:{filepath}")
