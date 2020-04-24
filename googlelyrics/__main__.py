import sys
from argparse import ArgumentParser

from .search import search


def parse_args():
    parser = ArgumentParser()

    parser.add_argument("--no-header", action="store_true",
                        help="don't print the info header")
    parser.add_argument("query", type=str, nargs="+",
                        help="search query")

    return parser.parse_args()


# pylint: disable=broad-except
def main():
    args = parse_args()

    try:
        text = search(" ".join(args.query), header=not args.no_header)
    except BaseException:
        sys.exit(sys.exc_info()[1])

    if not text:
        sys.exit("No lyrics found")

    print(text, end="")


if __name__ == "__main__":
    main()
