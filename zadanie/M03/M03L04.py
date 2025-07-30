# Rozwiń program z M02L11. Tamten program pytał użytkownika o tekst do zanonimizowania, czyli zastępował wszelkie występujące tam liczby iksami, np. 1234 -> XXXX. Tym razem zapytaj użytkownika o nazwę pliku (np. plik.txt) i wczytaj tekst właśnie z niego. Zanonimizuj go, a następnie wyświetl na ekranie.

# with open("/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/zadanie/M03/dokument_tekstowy.txt") as stream:
#     content = stream.read()
# print(content)

# anonymized = ""
# for char in content:
#     if char.isdigit():
#         anonymized += "x"
#     else:
#         anonymized += char

# print("DANE TAJNE: ", anonymized)

filname = "/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/zadanie/M03/dokument_tekstowy.txt"
with open(filname) as stream:
    text = stream.read()

for digit in "0123456789":
    text = text.replace(digit, "X")

print("DANE TAJNE: ")
print()
print(text)
       








