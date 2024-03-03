import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))


def process_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return stemmed_tokens


def main():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    processed_text = process_text(text)

    total_words_count = len(processed_text)

    word_count = Counter(processed_text)

    keyword_threshold = 4
    keywords = {word: count for word, count in word_count.items() if count >= keyword_threshold}

    keywords_counter = Counter(keywords)

    keywords_count = sum(keywords_counter.values())

    print(f"Total words count: {total_words_count}")
    print(f"Keywords count: {keywords_count}")


    print("\nKey words:")
    for word, count in keywords_counter.most_common():
        print(f"{word}: {count}")

    plt.bar(keywords_counter.keys(), keywords_counter.values())
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Keyword Frequency')
    plt.xticks(rotation=45)
    plt.show()


if __name__ == "__main__":
    main()
