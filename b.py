'''
Converts a string to a binary file.
Usage: python b.py <input_string> <file_name>
Example: python b.py "Hello World" hello.bin
'''

import sys

if len(sys.argv) != 3:
    print("Usage: python b.py <input_string> <file_name>")
    sys.exit(1)

input_string = sys.argv[1]
file_name = sys.argv[2]

with open(file_name, "wb") as binary_file:
    binary_file.write(input_string.encode())