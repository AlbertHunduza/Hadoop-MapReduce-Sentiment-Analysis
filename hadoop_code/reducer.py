import sys
import logging

logger = logging.getLogger()
word_count = {}
word_sentiment = {}

# input comes from STDIN
for line in sys.stdin:

    word, sentiment_score = line.strip().split()

    try:
        word_count[word] += 1
        word_sentiment[word] += int(sentiment_score)
    except KeyError:
        word_count[word] = 0
        word_sentiment[word] = int(sentiment_score)

for word, sentiment_score in word_sentiment.items():
    if word_count[word] > 15:
        if sentiment_score/word_count[word] != 1 and sentiment_score/word_count[word] != 0:
            print(f'{word}: {sentiment_score/word_count[word]}')