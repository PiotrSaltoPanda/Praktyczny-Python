filename = input("Wpisz nazwę pliku: ")

if "." in filename:
    name, extension = filename.rsplit(".", 1)
    print(f"Nazwa: {name}", f"Rozszerzenie: {extension}")
else:
    print(filename, "to nie nazwa pliku")

#--------------------------------------------------------------------------------

# Rozwiązanie według prowadzącego:

# NEW_EXTENSION = '.bak'

# filename = input("Podaj nazwę pliku: ")

# if '.' in filename:
#     tokens = filename.rsplit('.', maxsplit=1)
#     name = tokens[0]
#     extension = tokens[1]
# else:
#     name = filename
#     extension = ''

# new_filename = name + NEW_EXTENSION
# print(filename, '->', new_filename)