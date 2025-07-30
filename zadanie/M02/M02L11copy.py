# text = input("Podaj dane: ")
# result = ""
# for char in text:
#     if char.isdigit():
#         result += "X"
#     else:
#         result += char
# print("Dane popufne: ", result)

text = input("Podaj dane: ")
for digit in "0123456789":
    text = text.replace(digit, "x")
print("Dane poufne: ", text)