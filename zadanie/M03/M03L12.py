import glob
import os

NEW_EXTENSION = '.bak'

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)

for filename in filenames:
    if '.' in filename:
        tokens = filename.split('.', maxsplit=1)
        name = tokens[0]
        extension = tokens[1]
    else:
        name = filename
        extension = ''

    new_filename = name + NEW_EXTENSION
    os.rename(filename, new_filename)
    print(filename, '->', new_filename)