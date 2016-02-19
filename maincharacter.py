import json
from collections import defaultdict
from collections import Counter
from operator import itemgetter

books = defaultdict(Counter)

with open('conversations.jsonl', 'r') as f:
    for line in f:
        chain = json.loads(line)
        characters = set(map(itemgetter(0), chain['conversation']))
        for character in characters:
            books[chain['book_title']][character] += 1

for book in books:
    print('\033[1m' + book + '\033[0m', books[book].most_common(5), sep=' ')
