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
        word_count[word] = 1  # Corrected initialization to 1
        word_sentiment[word] = int(sentiment_score)

# Sort the words by average sentiment score in descending order
sorted_words = sorted(word_sentiment.keys(), key=lambda x: word_sentiment[x] / word_count[x], reverse=True)

# Print the result in a tabular format
print("{:<15}{}".format("Word/Token", "Average Sentiment Score"))
print("-" * 38)

for word in sorted_words:
    if word_count[word] > 15:
        average_sentiment = word_sentiment[word] / word_count[word]
        print("{:<15}{:.2f}".format(word, average_sentiment))
