import json
import pandas
from collections import Counter
import matplotblib

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

<<<<<<< HEAD
print(lengths.keys(), lengths.values())
data = pandas.DataFrame.from_dict(lengths, orient='index')
print(data.dtypes)
data.plot()

=======
# Frequency of lengthy conversations overall (Zipf-y)
print(lengths)
>>>>>>> 6989ea8295b5eebfc03696a19de24522d4c53f04
