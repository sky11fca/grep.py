import sys
from modules.directory_parse import directory_parse

def main(pattern, path, flags):
    FLAGS = {"-ignoreCase": 0}
    for flag in flags:
        if flag in FLAGS.keys():
            FLAGS[flag] = 1
        else:
            print("Invalid flag")

    success = directory_parse(pattern, path, FLAGS)
    sys.exit(0 if success else 1)

