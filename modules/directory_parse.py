import os

from modules.file_parse import file_parse
def directory_parse(pattern, path, FLAGS):
    # If is a directory, will go to the next item
    # Else, will parse the file instead

    valid_extension = text_extensions = {
        '.txt', '.py', '.js', '.java', '.cpp', '.c', '.h', '.hpp',
        '.html', '.css', '.xml', '.json', '.yml', '.yaml', '.md',
        '.csv', '.tsv', '.log', '.cfg', '.conf', '.ini', '.sh',
        '.bat', '.ps1', '.sql', '.rst', '.bib'
    }

    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension not in valid_extension: continue
                file_parse(pattern, os.path.join(root, file, FLAGS))
    else:
        file_parse(pattern, path, FLAGS)

    return True