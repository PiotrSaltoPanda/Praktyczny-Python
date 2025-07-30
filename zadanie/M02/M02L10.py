# Napisz program, który prosi użytkownika o hasło, a następnie dla każdego znaku wyświetla jakiego typu jest to znak (litera vs cyfra vs biały znak vs znak specjalny).

text = input("Podaj hasło: ")
for char in text:
    if char.isalpha():
        print(f"'{char}' - Litera")
    elif char.isdigit():
        print(f"'{char}' - Cyfra")
    elif char.isspace():
        print(f"'{char}' - Biały znak")
    else:
        print(f"'{char}' - Znak specjalny")


# for i in range(1, 11):
#     if i % 3 == 0:
#         print(i,"fizz")
#     elif i % 5 == 0:
#         print(i,"buzz")






    


    