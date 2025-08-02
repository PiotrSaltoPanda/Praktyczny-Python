# FILES = ["Koszty dodatkowe.txt", "Niespodzianki.txt"]

# for products in FILES:
#     print(products)

#     with open(products, "r") as cookbook:
#         recipe = cookbook.read()

#     lines = recipe.split("\n")
#     print(lines)

#     for line in lines:
#         if line.strip() and ":" not in line:
#             parts = line.split()
#             if len(parts) >= 2 and parts[-2].replace(".","").isdigit():
#                 kwota = parts[-2]
#                 opis = " ".join(parts[:-2])
#                 print(f"kwota: {kwota}, Opis: {opis}")

# empty = []
# if empty:
#     print("nie pusta")
# else:
#     print("pusta")

#-----------------------------------------------------------------------
# kod uproszczony:

files = ["Koszty dodatkowe.txt", "Niespodzianki.txt"]

for file in files:
    print(file)
    with open(file) as f:
        content = f.read()
    
    for line in content.split("\n"):
        if line and ":" not in line and "zł" in line:
            words = line.split()
            kwota, opis = words[-2], " ".join(words[:-2])
            print(f"kwota: {kwota}, Opis: {opis}")

print("pusta")

#----------------------------------------------------------------------
# rozwiązanie zadania:

# EXPENSE_FILENAME = "M03/expenses_ex.txt"

# with open(EXPENSE_FILENAME) as stream:
#     content = stream.read()

# lines = content.split('\n')

# total = 0
# for line in lines:
#     tokens = line.split()
#     if tokens:
#         expense = tokens[0]
#         total += float(expense)
# print('Suma wydatków: ', total)