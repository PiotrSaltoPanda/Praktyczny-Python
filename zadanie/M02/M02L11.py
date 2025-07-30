

text = input("Podaj dane: ")
for digit in "0123456789":
    text = text.replace(digit, "x")
print("Dane poufne: ", text)
