# # Napisz program, który prosi o jeden, pojedynczy znak, a następnie wyświetla, czy jest to liczba, litera, biały znak czy znak specjalny.
# # Białe znaki to spacja, tabulacja i nowa linia.

command = input("wpisz znak aby go zinterpretować: ")
if len(command) < 1:
    print("Podaj tylko jeden znak!")
elif len(command) > 1:
    print("Podaj jeden znak")
elif command.isdigit():
    print("To jest liczba.")
elif command.isalpha():
    print("To jest litera.")
elif command.isspace():
    print("To jest biały znak.")
elif command.startswith(('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/')):
    print("To jest znak specjalny.")
else:
    print("Nie rozpoznano znaku.")



# Napisz kalkulator BMI. Użytkownik podaje wagę i wzrost, a program wyświetla wynik wraz z komentarzem. BMI jest liczone jako waga podzielona przez wzrost w metrach do kwadratu. Jeśli BMI jest między 18.5 a 25, to napisz, że jest ono w normie. W przeciwnym razie napisz, że jest to niedowaga lub nadwaga, a dla BMI > 30 otyłość.

# weight = float(input("Podaj swoją wagę w kilogramach: "))
# height = float(input("Podaj swój wzrost w metrach: "))
# bmi = weight / height**2
# print("Twoje BMI wynosi: ", round(bmi, 2))
# if bmi < 18.5:
#     print("Masz niedowagę.")
# elif 18.5 <= bmi < 25:
#     print("Masz wagę w normie.")
# elif 25 <= bmi <= 30:
#     print("Masz nadwagę.")
# else:
#     print("Masz otyłość")



# Kalkulator wieku psa. Napisz program, który na podstawie wieku psa podanego przez użytkownika wyliczy jego wiek w latach ludzkich. Pierwsze dwa lata życia psa zawsze odpowiadają ok. 10,5 ludzkich lat (1 psi rok = 10.5 ludzkich lat, 2 psie lata = 21 ludzkich lat), a każdy kolejny rok życia psa to ok. 4 ludzkie lata.

# age = float(input("Podaj wiek psa w latach ludzkich: "))
# if age < 0:
#     print("Wiek psa nie moze być ujemny")
# elif age == 0:
#     print("Psa nie ma jeszcze na świecie.")
# elif age <= 2:
#     dog_age = age * 10.5
# elif age > 2:
#     dog_age = 21 + (age - 2) * 4
#     print("Wiek psa w latach psich wynosi: ", (dog_age))

