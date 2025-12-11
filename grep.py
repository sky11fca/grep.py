import argparse
import sys
from main import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a pattern in a directory")
    parser.add_argument("pattern", help="The pattern to search for")
    parser.add_argument("path", help="The path to search in")
    parser.add_argument("-i", "--ignoreCase", action="store_true", help="Ignore case sensitivity")

    args = parser.parse_args()

    flags = {"-ignoreCase": args.ignoreCase}


    main(args.pattern, args.path, flags=flags)