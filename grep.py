import sys
from main import main

if len(sys.argv) != 3:
    with open("Help.Txt", "r") as f:
        print(f.read())
    sys.exit(1)

if __name__ == "__main__":
    pattern = sys.argv[1]
    path = sys.argv[2]
    main(pattern, path)