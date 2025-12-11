import argparse
import sys
from main import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a pattern in a directory")
    parser.add_argument("pattern", help="The pattern to search for")
    parser.add_argument("paths", nargs="+", help="The path to search in")
    parser.add_argument("-ignoreCase", action="store_true", help="Ignore case sensitivity")
    parser.add_argument("-not", dest="invert_match", action="store_true", help="List lines that do not match with the regex")
    parser.add_argument("-count", action="store_true", help="Counts the number of lines that match with the pattern.")


    args = parser.parse_args()

    flags = {
        "-ignoreCase": args.ignoreCase,
        "-not": args.invert_match,
        "-count": args.count
    }


    main(args.pattern, args.paths, flags=flags)