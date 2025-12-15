# Python project: grep.py

---

## Index:

---

- [usage](#Usage)
- [options](#options)
- [regex pattern](#regex-pattern)
- [examples](#examples)
  - [basic](#basic-examples)
  - [advanced](#advanced-examples)
- author

---

## Usage

---

```bash
python grep.py <regex pattern> [paths/to/dir/or/file] [options]
```

---

## Options

---

`-ignoreCase`: Parses through files given a regex pattern no matter the case.

`-not`: Parses through files given a regex pattern that do not match.

`-count`: Counts the number of matches per file.

---

## Regex Pattern

---

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

---

## Examples

---

### Basic Examples:

---

**Search for a pattern in a file**

---

``` bash
python grep.py "fox" ./samples/sample_text.txt
```

``` 
1) The quick brown fox jumps over the lazy dog.
4) The dog chased the fox.
```

``` bash
python grep.py "fox" ./samples/sample_text.txt -ignoreCase
```

``` 
1) The quick brown fox jumps over the lazy dog.
2) Foxes are quick and brown.
4) The dog chased the fox.
```

```bash
python grep.py "fox" ./samples/sample_text.txt -not
```

```aiignore
2) Foxes are quick and brown.
3) DOG is man's best friend.
5) Quick, quick, quick!
6) The end.
```

```
python grep.py "fox" ./samples/sample_text.txt -not -count
```

``` 
file samples/sample_text.txt has 4 instances
Total Matches: 4
```

---

**Search for a pattern in a directory containing files**


---

``` 
 python grep.py "^py*|^def" ./samples/ -ignoreCase
```

```aiignore
samples/sample_python_script.py
5) def calculate_total(items):
samples/sample_readme.md
8) pip install -r requirements.txt
9) python setup.py install
```

```bash
python grep.py "^py*|^def" ./samples/ -ignoreCase -count
```

```aiignore
file samples/sample_python_script.py has 1 number of instances
file samples/sample_readme.md has 2 number of instances
Total Matches: 3
```


---

### Advanced examples:


---

```bash
python grep.py "[A-Z]{3}" ./samples/sample_text.txt 
```

```aiignore
./samples/sample_text.txt
3) DOG is man's best friend.
```

```bash
python grep.py "INFO|WARN|ERROR|DEBUG" ./samples/sample_log.txt 
```
```aiignore
1) [2024-01-15 08:30:15] INFO: Server started successfully
2) [2024-01-15 08:31:22] ERROR: Database connection failed
3) [2024-01-15 08:32:45] WARN: High memory usage detected
4) [2024-01-15 08:33:10] INFO: User 'admin' logged in
5) [2024-01-15 08:35:55] ERROR: File not found: /var/www/index.html
6) [2024-01-15 08:40:20] DEBUG: Processing request ID 12345
7) [2024-01-15 08:45:30] INFO: Backup completed
```

```bash
 python grep.py "ID \d{5}" ./samples/sample_log.txt 
```

```aiignore
6) [2024-01-15 08:40:20] DEBUG: Processing request ID 12345
```

```bash
python grep.py "def \w+\(" ./samples/sample_python_script.py
```

```aiignore
5) def calculate_total(items):
17)     def __init__(self, data):
20)     def filter_data(self, threshold=10):
24)     def compute_stats(self):
```

```bash
python grep.py "__\w+__" ./samples/sample_python_script.py 
```

```aiignore
./samples/sample_python_script.py
17)     def __init__(self, data):
36) if __name__ == "__main__":
```

---

## Author

---

Project created by Bazon Bogdan for the Python Programming course.