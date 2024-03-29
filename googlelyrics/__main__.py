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

    lyrics = search(" ".join(args.query))

    if not lyrics:
        sys.exit("No lyrics found")

    if not args.no_header:
        print(f"{lyrics.artist} - {lyrics.title}\n")

    print("\n".join(lyrics.lines))


if __name__ == "__main__":
    main()
