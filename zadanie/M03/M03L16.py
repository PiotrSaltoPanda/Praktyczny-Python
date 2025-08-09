# import glob
# import os

# pattern = input("Podaj pattern: ")
# filenames = glob.glob(pattern)
# changes = []

# print("Zostaną zmienione następujące pliki: ")
# for filename in filenames:
#     if '.' in filename:
#         name, old_extension = filename.rsplit('.', 1)
#         new_filename = name + '.bak'
#         print(f"  {filename} -> {new_filename}")
#     else:
#         new_filename = filename + '.bak'
#     changes.append((filename, new_filename))
    
# choice = input('Czy kontynuować? [t/n]')

# if choice.lower() == 't':
#     for old, new in changes:
#         os.rename(old,new)
#     print(":-) Sukces")
# else:
#     print(":-( Anulowano")

#--------------------------------------------------------------

# rozwiązanie:

import glob
import os
NEW_EXTENSION = '.bak'

pattern = input("Podaj pattern: ") #*.old
filenames = glob.glob(pattern)
operations = []

for filename in filenames:
    if "." in filename:
        tokens = filename.rsplit(".", maxsplit=1)
        name, extension = tokens
    else:
        name = filename
        extension = ""

    new_filename = name + NEW_EXTENSION
    operation = [filename, new_filename]
    operations.append(operation)

print("ZOSTANĄ DOKOŃCZONE NASTĘPUJĄCE ZMIANY: ")
for old, new in operations:
    print(old, "->", new)

choice = input("Czy kontynuowaĆ? [t/n] ")
if choice.lower() == "t":
    for old, new in operations:
        os.rename(old,new)
        print("Zmieniono", old, "->", new)
    print(":-) Sukces")