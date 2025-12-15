import re, time

def file_parse(pattern, filename, FLAGS):

    flags = re.IGNORECASE if FLAGS["-ignoreCase"] else 0
    invert_match = FLAGS["-not"]
    count_mode = FLAGS["-count"]

    try:
        compiled_pattern = re.compile(pattern, flags)
    except re.error as e:
        with open("grep.log", "a") as f:
            f.write(f"REGEX error for pattern '{pattern}' in file '{filename}'\n")
        print(e)
        return 0

    try:
        start_time = time.time()

        with open("grep.log", "a") as f:
            f.write(f"Processing file '{filename}'\n")

        match_output = 0
        with open(filename, 'r') as file:
            printed_filename = False
            for line_nr, line in enumerate(file, start=1):
                line = line.rstrip("\n")

                is_match = compiled_pattern.search(line)
                if invert_match:
                    is_match = not is_match

                if is_match:
                    match_output += 1
                    if not count_mode:
                        if not printed_filename:
                            print(f"{filename}")
                            printed_filename = True

                        if not invert_match:
                            line = compiled_pattern.sub(f"\033[91m\g<0>\033[0m", line)
                        print(f"{line_nr}) {line}")

            if count_mode and match_output > 0:
                print(f"file{filename} has {match_output}")

        end_time = time.time()
        with open("grep.log", "a") as f:
            f.write(f"File '{filename}' processed in {end_time - start_time:.4f} seconds\n")
        return match_output

    except FileNotFoundError:
        with open("grep.log", "a") as f:
            f.write(f"File not found '{filename}'\n")
        print(f"File {filename} not found")
        return 0
    except IOError as e:
        with open("grep.log", "a") as f:
            f.write(f"IO Exception over '{filename}'\n")
        print(e)
        return 0
    except UnicodeDecodeError as e:
        with open("grep.log", "a") as f:
            f.write(f"Unicode Decode Exception: '{filename}' not decoded\n")
        print(f"Error decoding file {filename}: {e}")
        return 0
