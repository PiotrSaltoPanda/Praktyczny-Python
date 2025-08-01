FILENAME = "Naukowy tekst.txt"
PUNCTION = ".,?![]{}()\"'"

tekst = "sukces to tylko 10 % motywacji, a 90 % dyscypliny"

with open(FILENAME, "w") as writer:
    writer.write(tekst)

with open(FILENAME, "r") as stream:
    content = stream.read()

words = content.split()
total_words = len(words)
number_count = 0

for word in words:
    clean_word = word
    for punct in PUNCTION:
        clean_word = clean_word.replace(punct, "")

    try:
        float(clean_word)
        number_count += 1
    except ValueError:
        pass

print(f"W twoim tekście liczby pojawiają się {number_count} razy.")
print(f"Twój tekst brzmi naukowo w {(number_count / total_words) * 100:.1f}%")



