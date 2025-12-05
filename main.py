import sys
from modules.file_parse import file_parse

def main(pattern, path):
    success = file_parse(pattern, path)
    sys.exit(0 if success else 1)

