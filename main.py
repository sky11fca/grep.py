import sys
from modules.directory_parse import directory_parse

def main(pattern, path, flags):
    success = directory_parse(pattern, path, flags)
    sys.exit(0 if success else 1)

