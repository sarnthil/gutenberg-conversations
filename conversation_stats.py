import json
from collections import Counter

booksum, booknum = Counter(), Counter()
bookmeans = Counter()
lengths = Counter()

with open("conversations.jsonl") as f:
    for line in f:
        chain = json.loads(line)
        booksum[chain['book_title']] += len(chain['conversation'])
        booknum[chain['book_title']] += 1
        lengths[len(chain['conversation'])] += 1

for book in booksum:
    bookmeans[book] = booksum[book]/booknum[book]

# Average length of conversation by book:
print(bookmeans)

# Frequency of lengthy conversations overall (Zipf-y)
print(lengths)
