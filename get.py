#!/usr/bin/env python3
"""Get data from a URL using a CLI"""

from argparse import ArgumentParser, Namespace
from urllib.request import urlopen


def parse_args() -> Namespace:
    """
    Parse command line arguments. Use --help for help
    """
    parser = ArgumentParser()
    parser.add_argument("url", type=str, help="Location to download from")
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default="",
        help="Optional file path to write to. If not provided,\
            write to stdout",
    )

    return parser.parse_args()


def download_file(url: str, output_path: str) -> None:
    """
    Download `url` to the provided output path.
    """
    with urlopen(url) as response:
        downloaded_contents = response.read().decode()
    if output_path == "":
        print(downloaded_contents, end="\n")
        return
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(downloaded_contents)
    print(f"Wrote downloaded content to `{output_path}`")


def main(args: Namespace) -> None:
    """Entry point for get.py"""
    download_file(args.url, args.path)


if __name__ == "__main__":
    main(parse_args())
