import glob

pattern = input("Podaj pattern: ")
filenames = glob.glob(pattern)

print(f"znaleziono {len(filenames)} plików")
for filename in filenames:
    print(f"  {filename}")

confirm = input("Kontynuować? (t/n)")

if confirm.lower() == 't':
    for filename in filenames:
        with open(filename, 'r') as stream:
            content = stream.read()
            lines = content.split('\n')
            first_line = lines[0]
            print(filename, ':', first_line)
    print(":-) Sukces")
else:
    print(":-( Anulowano")

#-----------------------------------------------------------

# Rozwiązanie:

# import glob

# pattern = input("Podaj pattern: ")
# filenames = glob.glob(pattern)

# print("Zostaną wyświetlone następujące pliki: ")
# for filename in filenames:
#     print(filename)

# choice = input('Czy kontynuować? [t/n]')

# if choice.lower() == 't':
#     for filename in filenames:
#         with open(filename, 'r') as stream:
#             content = stream.read()
#             lines = content.split('\n')
#             first_line = lines[0]
#             print(filename, '->', first_line)
#     print(":-) Sukces")
# else:
#     print(":-( Anulowano")