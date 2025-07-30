text = input("Tekst: ")
print("Liczba znaków:", len(text))

words = len(text.split())

division = len(text) / words
print("słowa w twoim tekście mają średnio: ", division, "znaków")
