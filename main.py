import sys
from modules.directory_parse import directory_parse

def main(pattern, paths, flags):
    total_matches = 0
    for path in paths:
        matches = directory_parse(pattern, path, flags)
        total_matches += matches

    if flags["-count"]:
        print(f"Total Matches{total_matches}")

    sys.exit(0)

