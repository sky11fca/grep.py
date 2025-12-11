import sys
import time

from modules.directory_parse import directory_parse

def main(pattern, paths, flags):

    start_time = time.time()

    total_matches = 0
    for path in paths:
        matches = directory_parse(pattern, path, flags)
        total_matches += matches

    if flags["-count"]:
        print(f"Total Matches{total_matches}")

    end_time = time.time()
    duration = end_time - start_time

    open("grep.log", "a").write(f"Execution ended. Processed {len(paths)} in {duration:.4f} seconds. Found: {total_matches}\n")

    sys.exit(0)

