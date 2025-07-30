# Bazując na rozwiązaniu poprzedniego ćwiczenia, zmodyfikuj program tak, że jeżeli użytkownik poda kilka znaków, wówczas wyświetl błąd, że użytkownik powinien podać tylko jeden znak. W przeciwnym przypadku program powinien działać tak samo jak do tej pory.

text = input("Wpisz znak: ")

if len(text) < 1:
        print("Error: Wpisz tylko jeden znak.")
elif len(text) > 1:
        print("Error: Wpisz tylko jeden znak.")
elif text.isalpha() and len(text) == 1:
    print("To jest litera.")
else:
    print("To nie jest litera.")



# text = input("Wpisz znak: ")
# if len(text) != 1:
#     print("Error: Wpisz tylko jeden znak.")
# elif text.isalpha():
#     print("To jest litera.")
# else:
#     print("To nie jest litera.")


