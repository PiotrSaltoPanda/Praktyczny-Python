# Mini ćwiczenie 1:

# m = int(input("Podaj liczbę wierszy (m): "))
# n = int(input("Podaj liczbę kolumn (n): "))

# for x in range(m):
#     for y in range (n):
#         print("*", end="")
#     print()

#---------------------------------------------------------------------------

# Mini ćwiczenie 2:

# print("Tabliczka mnozenia: ")
# print("=" * 50)

# for x in range(1, 11):
#     for y in range(1, 11):
#         wynik = x * y
#         print(f"{wynik:3}", end = ' |')
#     print()
#     print("-" * 50)

# Rozwiązanie mini ćwiczenie 2:

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end= '\t')
#     print()

#----------------------------------------------------------------------------

# Rozwiązanie głównego ćwiczenia:

FILENAME = "/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/M03/comments.txt"
PUNCTATIONS = ",.?!"

with open(FILENAME) as reader:
    content = reader.read()

lines = content.split('\n')
comments = []
for line in lines:
    line = line.lower()
    for punc in PUNCTATIONS:
        line = line.replace(punc, " ")
    words = line.split()
    comments.append(words)

words = input("Jakich słów szukasz: ")
words = words.lower().split()
counter = 0
# for comment in comments:
#     if any(word in comment for word in words):
#         counter += 1
for comment in comments:
    exists = False
    for word in words:
        if word in comment:
            exists = True
            break
    if exists:
        counter += 1

print(counter, 'komentarzy zwiera przynajmniej jedno ze słów: ', end=' ')
for word in words:
    print(word, end=' ')
print()