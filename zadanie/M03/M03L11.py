import glob

files = glob.glob('M03/M03L0*')
NEW_EXTENSION = '.bak'

for file in files:
    if '.' in file:
        tokens = file.rsplit('.', maxsplit=1)
        name = tokens[0]
        extension = tokens[1]
    else:
        name = file
        extension = ''

    new_filename = name + NEW_EXTENSION
    print(file, '->', new_filename)

#-------------------------------------------------------------

# import glob

# files = glob.glob('M03/M03L0*')
# NEW_EXTENSION = '.bak'

# for file in files:
#     if '.' in file:
#         name = file.rsplit('.', 1)[0]
#         new_filename = name + NEW_EXTENSION
#         print(file, '->', new_filename)
#     else:
#         print(file, '->', file + NEW_EXTENSION)