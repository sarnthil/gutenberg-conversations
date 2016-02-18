import json
import pandas
from collections import Counter
import matplotblib

with open("conversations.jsonl") as f:
    lengths = Counter(len(json.loads(line)['conversation']) for line in f)

print(lengths.keys(), lengths.values())
data = pandas.DataFrame.from_dict(lengths, orient='index')
print(data.dtypes)
data.plot()

