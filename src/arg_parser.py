# This is the main code of this project nr, and it manages running the code and
# outputting the results to LaTex.
import argparse


def parse_cli_args():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description="Optional app description")

    # Include argument parsing for default code.
    # Allow user to load a graph from file.
    parser.add_argument(
        "--ggl",
        dest="google_style_guide",
        action="store_true",
        help=(
            "boolean flag, determines whether the Google Style Guide for "
            "Bash rules are followed."
        ),
    )

    # Allow user to specify an infile.
    parser.add_argument("infile", nargs="?", type=argparse.FileType("r"))

    # Specify default argument values for the parser.
    parser.set_defaults(google_style_guide=True,)

    # Load the arguments that are given.
    args = parser.parse_args()
    return args
