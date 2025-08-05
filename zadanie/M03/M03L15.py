# pattern = input("Podaj pattern: ")
# columns = pattern.split('.')
# #     file_name = columns[0]
# #     extension = columns[1]
# file_name, extension = columns
# print("Columns: ", columns)

#-----------------------------------------

# list_of_lists = [
#     ['Zakupy.txt', 'Zakupy.bak'],
#     ['plik.txt', 'plik.bak']
#     ]

# for item in list_of_lists:
#     print(item)
#     old, new = item
#     print(old, '->', new)

#-----------------------------------------

# list_of_lists = [
#     ['Zakupy.txt', 'Zakupy.bak'],
#     ['plik.txt', 'plik.bak']
#     ]

# for old, new in list_of_lists:
#     print(old, '->', new)

#----------------------------------------

import glob
import os

NEW_EXTENSION = '.bak'

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)
for filename in filenames:
    if '.' in filename:
        tokens = filename.split('.', maxsplit=1)
        name, extension = tokens
    else:
        name = filename
        extension = ''

    new_filename = name + NEW_EXTENSION
    os.rename(filename, new_filename)
    print(filename, '->', new_filename)