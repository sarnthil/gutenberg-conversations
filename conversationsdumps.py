import sys, csv, json
from csvtool import CSV

'''Row(line_id='114', paragraph_id='51', character_id='10002-1', character_name='Tonnison', book_id='10002', book_title='The House on the Borderland by Hodgson', quote="`` Take care ! '' ")'''

with CSV(open("sortedquotes.csv", 'r')) as f, open("dumps.json", 'w') as g:
    characters = set()
    quotes = {}
    interval = 5
    lastline = -interval
    for row in f:
        current_line = int(row.line_id)
        if current_line - lastline >= interval or quotes.get('book_id', 'Laura') != row.book_id:
            if len(characters) > 1:
                quotes['last_line'] = lastline
                json.dump(quotes, g)
                g.write('\n')
            characters = set()
            quotes = {'conversation':[], 'book_id': row.book_id, 'book_title': row.book_title, 'first_line': current_line}
        # now we have to add the current quote
        quotes['conversation'].append([row.character_name, row.character_id, row.quote])
        characters.add(row.character_id)
        lastline = current_line
# {'book_id': '234324', 'conversation': [['Peter','234324-1', 'Hello! How are you?'], ['Sam', '234324-4', "I'm fine!"]], 'first_line':132, 'last_line': 354, 'book_title': 'The House on the Borderland by Hodgson'}
