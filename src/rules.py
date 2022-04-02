class Rules:
    """ """

    def __init__(self, ruleset=None):
        """Specifies the rules according to the given ruleset.

        :param ruleset: The user choice on which Bash style guide conventions
        are followed.
        """
        # If no ruleset is given, default to Google Shell Style Guide
        if ruleset is None:
            ruleset = "google_shell_style_guide"

        # Specify what characters are allowed in a function creation line.
        # () Capture group of things that are considered together.
        # [] Match any characters in this set.
        # a-z Uncapitalised letters a-z.
        # _ also allow underscores in first part of function creation line.
        # + Do not match on empty strings.
        # In essence: allow a-z and underscores, no spaces, no digits etc.
        # That description should be followed by () {, hence:
        # () Capture group of things that are required together.
        # \( Backslash escapes the next character, which is (, which is wanted.
        # \) Backslash escapes the next character, which is ), which is wanted.
        # The space means we want a space.
        self.re_function_declaration_chars = r"([a-z_])+(\(\) {)"
        # TODO: Include verification that no other characters follow this char.
        # TODO: Accommodate newline characters of various OS's.
        self.function_ending_char = "}"
