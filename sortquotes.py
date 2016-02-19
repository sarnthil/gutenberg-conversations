import csv
import operator
data = csv.reader(open("book_quotes.csv"), delimiter=',')
next(data)
sortedlist = sorted(data, key=operator.itemgetter(0))
sortedlist.sort(key=operator.itemgetter(4))
f = open("sortedquotes.csv","w")
w = csv.writer(f)
w.writerow(['line_id', 'paragraph_id', 'character_id', 'character_name', 'book_id', 'book_title', 'quote'])
for row in sortedlist:
    w.writerow(row)
f.close()
