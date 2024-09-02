#!/usr/bin/env python3
"""Get data from a URL using a CLI"""

from argparse import ArgumentParser, Namespace
from urllib.request import urlopen


def parse_args() -> Namespace:
    """
    Parse command line arguments. Use --help for help
    """
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "url",
        type=str,
        nargs="?",
        help="Location to download from",
    )
    group.add_argument(
        "--assist",
        "-a",
        action="store_true",
        help="Launch a CLI helper tool to autofill parts of\
            a url for you",
    )
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
    if url == "":
        return
    with urlopen(url) as response:
        downloaded_contents = response.read().decode()
    if output_path == "":
        print(downloaded_contents, end="\n")
        return
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(downloaded_contents)
    print(f"Wrote downloaded content to `{output_path}`")


def _get_choice() -> int:
    """Return user's choice, -1 for quit"""
    print("Options:\n1. Custom URL\n2. GitHub raw file download\n\n`q` to exit\n")
    while True:
        option = input("Choice: ")
        if option == "q":
            return -1
        if not option.isdigit():
            print("Make sure you enter a number")
            continue
        choice = int(option)
        if choice not in range(1, 2 + 1):
            print("That's not a valid choice")
            continue
        return choice


def _raw_github() -> str:
    """Assist a user in generating a raw github url"""
    url = "https://raw.githubusercontent.com/"
    url += input("GitHub account name: ")
    url += "/"
    url += input("GitHub repository name: ")
    url += "/"
    url += input("Branch name [enter for `main`]: ") or "main"
    url += "/"
    url += input("Path to file on GitHub: ")
    print(f"Download URL is {url}")
    return url


def assistant(path: str) -> tuple[str, str]:
    """Prompt the user to generate url"""
    if path == "":
        path = input("File save path [enter for stdout]: ")
    choice = _get_choice()
    if choice == -1:
        return "", ""
    if choice == 1:
        return input("Download URL: "), path
    if choice == 2:
        return _raw_github(), path
    raise ValueError("Invalid choice uncaught in _get_choice")


def main(args: Namespace) -> None:
    """Entry point for get.py"""
    url = args.url
    path = args.path
    if args.assist:
        url, path = assistant(path)
    download_file(url, path)


if __name__ == "__main__":
    main(parse_args())
