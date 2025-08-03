# text = "jeden skowronek wiosny nie czyni"
# words = text.split()

# lengths = []
# for word in words:
#     word_lenght = len(word)
#     lengths.append(word_lenght)
# print("lengths: ", lengths)

with open("Zakupy.txt", 'w') as writer:
    writer.write("Lista zakupów: \n5 zł chleb \n45 zł wędlina \n7 zł sól \n20 zł pomidory \n15 zł ziemniaki \n4.50 zł śmietana \n200 zł USB \n150 zł obudowa do telefonu \n300 zł blender")

# expenses = [5, 45, 7, 20, 15, 4.50, 200, 150, 300] 
# total = sum(expenses)
# print("Wszystkie wydatki razem wynoszą razem: ", total, "zł")
# print(f"Średni koszt twoich wydatków: ", total/len(expenses), "zł")

expenses = []

with open("Zakupy.txt", 'r') as reader:
    content = reader.read()

    for line in content.split("\n"):
        if line and "zł" in line:
            words = line.split()
            kwota = words[0]
            expenses.append(float(kwota))

total = sum(expenses)
minimum = min(expenses)
maximum = max(expenses)
print(f"Wszystkie wydatki: ", total, 'zł')
print(f"Minimalna kwota to: ", minimum, 'zł')
print(f"Największa kwota to: ", maximum, 'zł')
print(f"Średnia wydatków: {total/len(expenses):.2f} zł")

#-------------------------------------------------------------------------------------------------
# Rozwiązanie:

# EXPENSES_FILENAME = "Zakupy.txt"

# with open(EXPENSES_FILENAME) as stream:
#     content = stream.read()

# lines = content.split('\n')

# expenses = []
# for line in lines:
#     tokens = line.split()
#     if tokens:
#         expense = float(tokens[0])
#         expenses.append(expense)

# total = sum(expenses)
# minimum = min(expenses)
# maximum = max(expenses)
# average = total/len(expenses)

# print("Wszystkie wydatki wynoszą: ", total)
# print("Najmniejszy wydatek to: ", minimum)
# print("Największy wydatek to: ", maximum)
# print("Średni wydatek to: ", average)