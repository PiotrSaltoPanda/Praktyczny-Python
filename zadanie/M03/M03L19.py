import glob

POSITIVE_RECENZIONS = '/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/pos'
NEGATIVE_RECENZIONS = '/Users/admin/Documents/Praktyczny Python/Praktyczny_Python_materialy-2022-08-23/M03/data/aclImdb/train/neg'
PUNCTATIONS = ",<>/;:\\|()*"

positive = glob.glob(f"{POSITIVE_RECENZIONS}/*.txt")
negative = glob.glob(f"{NEGATIVE_RECENZIONS}/*.txt")

positive_reviews = []
negative_reviews = []

for positive_file in positive:
    with open(positive_file, 'r') as reader:
        content = reader.read()
        content = content.lower()
        content = content.replace('.', '\n').replace('!', '\n').replace('?', '\n')
        for punc in PUNCTATIONS:
            content = content.replace(punc, ' ')
        sentences = content.split('\n')
        for sentence in sentences:
            words = sentence.split()
            if words:
                positive_reviews.append(words)


for negative_file in negative:
    with open(negative_file, 'r') as reader:
        content = reader.read()
        content = content.lower()
        content = content.replace('.', '\n').replace('!', '\n').replace('?', '\n')
        for punc in PUNCTATIONS:
            content = content.replace(punc, ' ')
        sentences = content.split('\n')
        for sentence in sentences:
            words = sentence.split()
            if words:
                negative_reviews.append(words)

all_words = set()
for sentence in positive_reviews:
    for word in sentence:
        all_words.add(word)
for sentence in negative_reviews:
    for word in sentence:
        all_words.add(word)

word_sentiment = {}
for word in all_words:
    positive_count = 0
    for sentence in positive_reviews:
        if word in sentence:
            positive_count += 1

    negative_count = 0
    for sentence in negative_reviews:
        if word in sentence:
            negative_count += 1

    total_count = positive_count + negative_count
    if total_count > 0:
        sentiment = (positive_count - negative_count) / total_count
        word_sentiment[word] = sentiment

comments = input("Wpisz komentarz: ")
comments = comments.lower().split()

sentiment_sum = 0
analyzed_words = 0

print("\nAnaliza sentymentu Twojego komentarza: ")
for word in comments:
    clean_word = word
    for punc in PUNCTATIONS + '.!?':
        clean_word = clean_word.replace(punc, '')

    if clean_word in word_sentiment:
        sentiment = word_sentiment[clean_word]
        sentiment_sum += sentiment
        analyzed_words += 1

        if sentiment > 0.1:
            emoji = "😊"
        elif sentiment < -0.1:
            emoji = "😔"
        else:
            emoji = "😑"

        print(f"'{clean_word}': {sentiment:.3f} {emoji}")
    else:
        print(f"'{clean_word}': nieznane słowo ？")

if analyzed_words > 0:
    average_sentiment = sentiment_sum / analyzed_words
    print(f"\n📊WYNIK:")
    print(f"Średni sentyment: {average_sentiment:.3f}")

    if average_sentiment > 0.2:
        print("🍻 Twój komentarz jest POZYTYWNY!")
    elif average_sentiment < -.2:
        print("⛈️ Twój komentarz jest NEGATYWNY!")
    else:
        print("🤝 Twój komentarz jest NEUTRALNY!")
else:
    print("Nie udało się przeanalizować zadnego słowa")