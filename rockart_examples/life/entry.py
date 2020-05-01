import argparse

from rockart_examples import __version__


def main():
    pass

def entry():
    parser = \
        argparse.ArgumentParser(
            description="Conway's Game of Life - Rockart usage example"
        )
    if __version__ is not None:
        parser.add_argument(
            "-v", "--version",
            action="version",
            version=__version__,
            help="show version of Rockart Examples and exit"
        )
    parser.parse_args()

    exit_code_or_message = main()
    return exit_code_or_message
