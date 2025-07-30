#-----------------------------------------------------------------

# reader = open("/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/zadanie/M03/plik.txt")
# content = reader.read()
# reader.close()

# writer = open("plik2.txt", "w")
# writer.write(content)
# writer.write("\nNumer karty roewrowej AOF90166123\n")
# writer.write("Kod do klatki schodowej KLUCZYK: 5678#\n")
# writer.close()

# reader = open("plik2.txt", "r")
# full_content = reader.read()
# reader.close()

# anonymized_content = full_content
# for digit in "0123456789":
#     anonymized_content = anonymized_content.replace(digit, "x")

# writer = open("plik2.txt", "w")
# writer.write(anonymized_content)
# writer.closed

#------------------------------------------------------------------

# reader = open("/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/zadanie/M03/plik.txt")
# content = reader.read()
# reader.close()

# with open("plik.txt", "w") as writer:
#     writer.write(content)
#     writer.write("\nKod do kłódki do piwnicy: 2323")
# writer.close()

# reader = open("plik.txt", "r")
# full_content = reader.read()
# reader.close()

# anonymized_content = full_content
# for digit in "0123456789":
#     anonymized_content = anonymized_content.replace(digit, "X")

# writer = open("plik3.txt", "w")
# writer.write(anonymized_content)
# writer.close()

# print("sukces!")

#-------------------------------------------------------------------

input_filname = input("Podaj nazwę pliku wejśćiowego ")
output_filname = input("Podaj nazwę pliku wyjściowego ")

with open("plik.txt", "r") as reader:
    text = reader.read()

for digit in ("0123456789"):
    text = text.replace(digit, "X")

if output_filname == "":
    print("Zanonimizowany tekst: ")
    print()
    print(text)
else:
    with open(output_filname, "x") as writer:
        writer.write(text)
    print("zapisano do pliku")