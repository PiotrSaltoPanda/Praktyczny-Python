word = input("Jakiego słowa szukasz?:").lower()
filename = "/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/M03/comments.txt"

with open(filename, 'r') as reader:
    content = reader.read().lower()

    for char in ".,!?:;-()[]{}\"'":
        content = content.replace(char, " ")

    words_list = content.split()

    if word in words_list:
        count = words_list.count(word)
        print(f"Słowo '{word}' zostało znalezione!")
        print(f"Występuje {count} razy")
    else:
        print(f"Słowo '{word}' nie zostało znalezione")

# -----------------------------------------------------------

# rozwiązanie:

# INPUT_FILE = "/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/M03/comments.txt"
# PUNCTUATIONS = '.,!?'

# with open(INPUT_FILE) as stream:
#     content = stream.read()

# lines = content.split('\n')
# comments = []
# for line in lines:
#     line = line.lower()
#     for punc in PUNCTUATIONS:
#         line = line.replace(punc, ' ')
#     words = line.split()
#     comments.append(words)

# word = input('Jakiego słowa szukasz? ')
# counter = 0
# for comment in comments:
#     if word in comment:
#         counter += 1
# print("Słowo", word, "pojawiło się w", counter, "komentarzach.")
    
