import sys
from argparse import ArgumentParser

from . import search


def parse_args():
    parser = ArgumentParser(prog="googlelyrics")

    parser.add_argument(
        "--no-header", action="store_true", help="don't print the info header"
    )
    parser.add_argument("query", type=str, nargs="+", help="search query")

    return parser.parse_args()


# pylint: disable=broad-except
def main():
    args = parse_args()

    try:
        lyrics = search(" ".join(args.query))
    except BaseException:
        sys.exit(sys.exc_info()[1])

    if not lyrics:
        sys.exit("No lyrics found")

    if not args.no_header:
        print(f"{lyrics.artist} - {lyrics.title}\n")

    print("\n".join(lyrics.lines))
    print()


if __name__ == "__main__":
    main()
