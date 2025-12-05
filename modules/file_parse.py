import re, os

def file_parse(pattern, filename):
    try:
        compiled_pattern = re.compile(pattern)
    except re.error as e:
        print(e)
        return False


    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"{filename}")
            for line_nr, line in enumerate(file, start=1):
                line = line.rstrip("\n")

                if compiled_pattern.search(line):
                    print(f"{line_nr}) {line}")
    except FileNotFoundError:
        print(f"File {filename} not found")
        return False
    except IOError as e:
        print(e)
        return False
    except UnicodeDecodeError as e:
        print(f"Error decoding file {filename}: {e}")
        return False
    return True