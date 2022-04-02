## Entry point for this project, runs the project code and exports data if
# export commmands are given to the cli command that invokes this script.


## Import used functions.
# Project code imports.
from .arg_parser import parse_cli_args

## Parse command line interface arguments to determine what this script does.
args = parse_cli_args()

## Include trivial funciton to test main.
def add_two(x):
    return x + 2


## Run main code.
# TODO

## Run code to test Google Style Guide for Bash compliance.
if args.google_style_guide:
    print(f"The Google Style Guide for Bash conventions are used.")
