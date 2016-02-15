import json
import glob
import csv
import sys

if __name__ == '__main__':
    titles = {}
    with open('books.csv') as f:
        reader = csv.reader(f)
        for etextid, title in reader:
            titles[etextid] = title
        characters = {}
    with open('characters_meta.txt', 'w') as fout:
        writer = csv.writer(fout, delimiter=",")
        writer.writerow(['character_id', 'name', 'alternative_names', 'book_id', 'book_title'])
        for folder in glob.iglob('output/*'):
            _, number = folder.split("/")
            try:
                with open("{}/{}.book".format(folder, number)) as f:
                    book = json.loads(f.read())
                    for character in book["characters"]:
                        try:
                            mainname = max((name['n'] for name in character["names"]), key=len)
                        except ValueError:
                            print(character)
                            continue
                        alternatives = [name['n'] for name in character["names"] if name['n'] != mainname]
                        charid = '{}-{}'.format(number, character['id'])
                        title = titles.get(number, '')
                        writer.writerow([charid, mainname, ','.join(alternatives), number, title])
            except FileNotFoundError:
                continue
