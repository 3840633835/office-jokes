#!/bin/sh
# Determinism test: main.py must write byte-identical entry.txt on every run.
set -eu
cd "$(dirname "$0")"

rm -rf /tmp/office-jokes-det-a /tmp/office-jokes-det-b
mkdir -p /tmp/office-jokes-det-a /tmp/office-jokes-det-b

OUTPUT_DIR=/tmp/office-jokes-det-a python3 main.py
OUTPUT_DIR=/tmp/office-jokes-det-b python3 main.py

cmp /tmp/office-jokes-det-a/entry.txt /tmp/office-jokes-det-b/entry.txt
cmp /tmp/office-jokes-det-a/entry.txt entry.txt

# Gate: 1-199 characters, single line, no trailing newline.
python3 -c "
s = open('/tmp/office-jokes-det-a/entry.txt', encoding='utf-8').read()
assert 1 <= len(s) <= 199, len(s)
assert '\n' not in s and '\r' not in s, 'must be a single line'
assert s.strip() == s, 'no surrounding whitespace'
print('entry.txt OK:', len(s), 'chars')
"

rm -rf /tmp/office-jokes-det-a /tmp/office-jokes-det-b
echo "determinism: PASS"
