import sys
import string
import logging

logger = logging.getLogger()

# Read stop words from stopwords.txt file
stop_words = set()
with open('stopwords.txt', 'r') as f:
    for word in f:
        stop_words.add(word.strip())

# input comes from STDIN (standard input)
for line in sys.stdin:

    sentiment_score, sentence = line.strip().lower().split(':', 1)

    word_array = sentence.split()

    for idx, token in enumerate(word_array):
        new_token = token
        for symbol in token:
            if symbol in string.punctuation:
                new_token = new_token.replace(symbol, '')
        word_array[idx] = new_token

    for word in word_array:
        if len(word) > 0 and word not in stop_words:
            print(f'{word} {sentiment_score}')


