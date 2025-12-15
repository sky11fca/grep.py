# Python project: grep.py

## Index:
- usage
- options
- regex pattern
- examples
  - basic
  - advanced
    - text files
    - log files
    - conf files
    - python script files
- author

## Usage

```bash
python grep.py <regex pattern> [paths/to/dir/or/file] [options]
```

## Options

`-ignoreCase`: Parses through files given a regex pattern no matter the case.

`-not`: Parses through files given a regex pattern that do not match.

`-count`: Counts the number of matches per file.

## Regex Pattern

`.`: every character except newline.

`^`: matches the begining of a line.

`*`: matches 0 or more characters.

`?`: matches 0 or 1 character.

`+`: matches 1 or more characters.

`{int}`: matches exactly int characters.

`{int, int}`: matches exactly between int and int characters.

`[]`: a group of characters

`|`: or operator

`\d`: matches a digit

`\D`: matches anything but digits

`\s`: matches a whitespace character

`\S`: matches anything but whitespace characters

`\w`: matches a word character

`\W`: matches anything but word characters

`\`: escape character

`[^]`: groups that do not match

`[...-...]`: groups of characters interval