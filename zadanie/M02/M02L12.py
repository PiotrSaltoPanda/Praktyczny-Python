# Mini ćwiczenie 1

# counter = 0
# text = input("Podaj wyraz z jak największą ilością litery A: ")
# for char in text:
#     if char == "a" or char == "A":
#         counter = counter + 1
# print("Ilość A w tekście: ", counter)

# Rozwiązanie 1. minićwiczenia:

# text = input("Podaj tekst: ")
# counter = 0
# for char in text:
#     if char.lower() == 'a':
#         counter += 1
# print("Litera a pojawia się", counter, "razy")

# Mini ćwiczenie 2

# counter = 0
# text = input("Wpisz tekst z nawiasmi: ")
# for char in text:
#     if char == "(":
#         counter += 1
#     elif char == ")":
#         counter -= 1

#     if counter < 0:
#         print("Błąd, zamknięto nawias, który nie był otwarty. ")
#         break

# if counter > 0:
#     print(f"Błąd: Pozostało {counter} nie zamkniętych nawiasów>")
# elif counter == 0:
#     print("Nawiasy zostąły poprawnie sparowane.")

# Rozwiązanie 2. minićwiczenia:

# text = input("Podaj tekst: ")
# level = 0
# for char in text:
#     if char == '(':
#         level += 1
#     elif char == ')':
#         level -= 1
#     if level < 0:
#         print("Ups, wygląda na to, że zamykasz nawias zanim go otworzyłeś")
# if level > 0:
#     print("Ups, brakuje jednego lub kilku nawiasów zamykających")

# Mini ćwiczenie 3


# player1 = input("Gracz nr 1, papier, nozyce, kamień: ")
# player2 = input("Gracz nr 2. papier, nozyce, kamień: ")

# if player1 == player2:
#     print("Remis!")
# elif (player1 == "papier" and player2 == "kamień") or \
#      (player1 == "nozyce" and player2 == "papier") or \
#      (player1 == "kamień" and player2 == "nozyce"):
#     print("Gracz 1 wygrywa!")
# else:
#     print("Gracz 2 wygrywa!")

# Rozwiązanie 3. minićwiczenia:

# user_choice = input("Twój ruch: ")
# computer_choice = input("Ruch przeciwnika: ")
# if user_choice == computer_choice:
#     print("Remis!")
# else:
#     if user_choice == "kamień":
#         if computer_choice == "papier":
#             print("Przegrałeś!")
#         else:
#             print("Wygrałeś!")
#     elif user_choice == "papier":
#         if computer_choice == "nożyce":
#             print("Przegrałeś!")
#         else:
#             print("Wygrałeś!")
#     elif user_choice == "nożyce":
#         if computer_choice == "kamień":
#             print("Przegrałeś!")
#         else:
#             print("Wygrałeś!")

# Alternatywne rozwiązanie 3. minićwiczenia:

# user_choice = input("Twój ruch: ")
# computer_choice = input("Ruch przeciwnika: ")
# if user_choice == "kamień":
#     if computer_choice == "nożyce":
#         print("Wygrałeś!")
#     elif computer_choice == "kamień":
#         print("Remis")
#     elif computer_choice == "papier":
#         print("Przegrałeś")
# elif user_choice == "nożyce":
#     if computer_choice == "papier":
#         print("Wygrałeś!")
#     elif computer_choice == "nożyce":
#         print("Remis")
#     elif computer_choice == "kamień":
#         print("Przegrałeś")
# elif user_choice == "papier":
#     if computer_choice == "kamień":
#         print("Wygrałeś!")
#     elif computer_choice == "papier":
#         print("Remis")
#     elif computer_choice == "nożyce":
#         print("Przegrałeś")

# ćwiczenie główne:

counter = 0
text = input("Wprowadź hasło: ")
for char in text:
    if char.isalpha() or char.isdigit():
        counter = counter + 1

if len(text) <= 7:
    print("Hasło musi zawierać conajmniej 8 znaków.")

isdigit_counter = 0
for char in text:
    if char.isdigit():
        isdigit_counter += 1

special_counter = 0
for char in text:
    if not char.isalpha() and not char.isdigit() and not char.isspace():
        special_counter += 1

if special_counter == 0:
    print("Hasło musi zawierać minimum 1 znak specjalny.")

isspace_counter = 0
for char in text:
    if char.isspace():
        isspace_counter += 1

if isspace_counter > 0:
    print("Hasło nie moze zawierać znaku 'spacja'.")

islower_counter = 0
for char in text:
    if char.islower():
        islower_counter += 1

if islower_counter == 0:
    print("Hasło musi zawierać minimum jedną małą literę.")

isupper_counter = 0
for char in text:
    if char.isupper():
        isupper_counter += 1

if isupper_counter == 0:
    print("Hasło musi zawierać minimum jedną wielką literę.")

print("Twoje hasło ma", len(text), "znaków, w tym", islower_counter, "małych liter", isupper_counter, "wielkich liter,", isdigit_counter, "cyfr, oraz", special_counter, "znaków specjalnych")


#    elif not char.isdigit(): # ✅ Jak nie mała ani wielka litera ani spacja, to znaczy że mamy cyfrę albo znak specjalny.

#         has_special_char = True
    

    
