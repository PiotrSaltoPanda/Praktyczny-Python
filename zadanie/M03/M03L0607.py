# Mini ćwiczenienr 1:

# counter = 0
# with open("plik.txt", "r") as reader:
#     content = reader.read()

# words = content.split()
# for word in words:
#     if word.isalpha():
#         counter += 1

# print(f"Liczba słów w tekście: {counter}")

#----------------------------------------------------------------------------------------------------------------------------------

# Mini ćwiczenie nr 2:

# counter = 0
# with open("plik.txt", "r") as reader:
#     content = reader.read()

# words = content.split()
# for word in words:
#     if any(char.isupper() for char in word):
#         counter += 1

# print(f"Liczba wyrazów zaczynających się z wielkiej litery to: {counter}")

#----------------------------------------------------------------------------------------------------------------------------------

# Mini ćwiczenie nr 3:

# with open("plik.txt", "r") as reader:
#      content = reader.read()

# words = content.split()
# number_count = 0

# for word in words:
#     try:
#         cost = float(word.replace(",","."))
#         if cost > 0:
#          number_count += 1
#          print(f"Liczby dodatnie: {cost}")
#     except ValueError:
#         pass

# print(f"Znaleziono liczb dodatnich w pliku: ", number_count)



#----------------------------------------------------------------------------------------------------------------------------------

# Ćwiczenie główne wersja samodzielna:

with open("Lista wydatków.txt", "w") as writer:
    writer.write("Lista miesięcznych wydatków:\nMieszkanie 7000 zł\nJedzenie 4000 zł\nTelefon 150.50 zł\nBenzyna 800 zł\nUbezpieczenie 1600 zł\nPraktyczny Python 400 zł")

with open("Koszty dodatkowe.txt", "w") as writer:
    writer.write("Koszty dodatkowe:\nSzafka z Ikei 550.50 zł\nUrodziny znajomego 200 zł")

with open("Niespodzianki.txt", "w") as writer:
    writer.write("Niespodzianki:\nZarysowany zderzak w aucie 1000 zł\nNaprawa telefonu 400 zł")

files = ["Lista wydatków.txt", "Koszty dodatkowe.txt", "Niespodzianki.txt"]
all_costs = []

for filename in files:
    with open(filename, "r") as reader:
        content = reader.read()

    words = content.split()
    for word in words:
        try:
            cost = float(word.replace(",", "."))
            all_costs.append(cost)
            print(f"Koszt: {cost} zł z pliku {filename}")
        except ValueError:
            pass

                  
# print("\nWszystkie koszty:", all_costs)
# print("Suma:", sum(all_costs), "zł")

#----------------------------------------------------------------------------------------------------------------------------------

# Ćwiczenie główne wersja z lekcji:

# expenses = [100, 200, 300, 150, 1000]
# total = 0
# for expense in expenses:
#     total = total + expense

# print("Wszystkie wydatki wynoszą razem: ", total, "zł")
