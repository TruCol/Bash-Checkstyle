def pytest_addoption(parser):
    """
    Parses CLI arguments to run specific (groups of) tests. Running:
    python -m pytest runs the default tests pertaining to the main code of
    this project. Including the argument --ggl runs the main code
    tests as well as tests that pertain to the Google Style Guide for Bash
    conventions.
    :param parser: The object containing the arguments that are passed from the
    command line interface (CLI).

    """
    # Runs tests of main code, as well as tests pertaining to
    # google_style_guide_tests code.
    parser.addoption(
        "--ggl",
        action="store_true",
        dest="google_style_guide_tests",
        default=False,
        help="enable google_style_guide_tests tests",
    )


def pytest_configure(config):
    """
    Sets the keywords, like @google_style_guide_tests_tests that are used to
    run or not run (groups of) tests.

    :param config: Object representing which tests are and are not ran by
    pytest.

    """
    if not config.option.google_style_guide_tests:
        setattr(config.option, "markexpr", "not google_style_guide_tests")
