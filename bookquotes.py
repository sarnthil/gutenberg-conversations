import json
import glob
import csv
import sys
from collections import namedtuple

if __name__ == '__main__':
    csv.field_size_limit(sys.maxsize)
    titles = {}
    with open('books.csv') as f:
        reader = csv.reader(f)
        for etextid, title in reader:
            titles[etextid] = title
        characters = {}
    with open('book_quotes.csv', 'w') as fout:
        writer = csv.writer(fout, delimiter=",")
        writer.writerow(['line_id','paragraph_id','character_id', 'character_name', 'book_id', 'book_title', 'quote'])
        for idx, folder in enumerate(glob.iglob('output/*')):
            print("%.2f percent " % ((idx+1)/926), end='     \r')
            _, number = folder.split("/")
            try:
                with open("{}/{}.book".format(folder, number)) as bookf, open('tokens/'+number, "rt") as tokenf:
                    wordlookup = {}
                    tokenreader = csv.reader(tokenf, delimiter='\t', quotechar='ă')
                    Data = namedtuple("Data", next(tokenreader))
                    for stuff in tokenreader:
                        try:
                            data = Data(*stuff)
                        except:
                            print(stuff)
                            print(number)
                            sys.exit()
                        wordlookup[int(data.tokenId)] = (data.sentenceID, data.paragraphId)
                        # print(type(data.tokenId))
                    book = json.loads(bookf.read())
                    for character in book["characters"]:
                        try:
                            mainname = max((name['n'] for name in character["names"]), key=len)
                        except ValueError:
                            # print(character)
                            continue
                        charid = '{}-{}'.format(number, character['id'])
                        title = titles.get(number, '')
                        for quote in character["speaking"]:
                            # print(type(quote['i']))
                            lineid, parid = wordlookup[quote['i']]
                            writer.writerow([lineid, parid, charid, mainname, number, title, quote['w']])
            except FileNotFoundError:
                continue
