import json
from collections import Counter

with open("conversations.jsonl") as f:
    lengths = Counter(len(json.loads(line)['conversation']) for line in f)

print(lengths)
print(lengths.keys(), lengths.values())
