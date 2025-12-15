import os

from modules.file_parse import file_parse
def directory_parse(pattern, path, flags):
    # If is a directory, will go to the next item
    # Else, will parse the file instead

    valid_extension = text_extensions = {
        '.txt', '.py', '.js', '.java', '.cpp', '.c', '.h', '.hpp',
        '.html', '.css', '.xml', '.json', '.yml', '.yaml', '.md',
        '.csv', '.tsv', '.log', '.cfg', '.conf', '.ini', '.sh',
        '.bat', '.ps1', '.sql', '.rst', '.bib'
    }

    total_count = 0

    if not os.path.exists(path):
        with open("grep.log", "a") as f:
            f.write(f"File or directory not found: '{path}'\n")
        print(f"Invalid path: '{path}' (it doesn't exist)")
        return 0

    try:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    extension = os.path.splitext(file)[1]
                    if extension not in valid_extension: continue
                    total_count += file_parse(pattern, os.path.join(root, file), flags)
        else:
            extension = os.path.splitext(path)[1]
            if extension in valid_extension:
                total_count += file_parse(pattern, path, flags)
    except PermissionError as e:
        with open("grep.log", "a") as f:
            f.write(f"Permission denied: '{path}'\n")
        print(f"Permission denied: '{path}': {e}")
        return 0

    except OSError as e:
        with open("grep.log", "a") as f:
            f.write(f"OS error: '{path}'\n")
        print(f"OS error: '{path}': {e}")
    return total_count