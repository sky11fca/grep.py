import sys
from main import main

if len(sys.argv) != 4:
    with open("Help.txt", "r") as f:
        print(f.read())
    sys.exit(1)

if __name__ == "__main__":
    pattern = sys.argv[1]
    path = sys.argv[2]
    flags = sys.argv[3:]
    main(pattern, path, flags=flags)