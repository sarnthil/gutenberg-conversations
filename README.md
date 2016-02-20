# gutenberg-conversations
This corpus contains a collection of fictional conversations extracted from raw novels of The Gutenberg Project.
The files used to create it were obtained using the [book-nlp](https://github.com/dbamman/book-nlp).

- 86185 conversational exchanges between pairs of movie characters
- involves 67942 characters from 928 novels
- in total 578213 utterances
- novel metadata not included yet: %TO DO:
	✗ genres
	✗ Goodreads rating
- character metadata not included: %TO DO:
	✗ gender (for all characters)
	✗ position on novel hierarchy

## Files

In all files the field separator is ","

- characters_meta.csv
	- info about characters
	- fields:
		- ✓ `character_id`
		- ✓ `character_name` (after clustering)
		- ✓ `book_id`
		- ✓ `book_title`
		- ✗ gender ("_" for unknown cases)
		- ✗ other traits: position in a hierarchy, sentiment, adjectives/adverbs that are most frequent used by those characters, networks of relationships to others, ...

- books_quotes.csv
	- contains the actual text of each quote
- fields:
	- ✓ `line_id`
	- ✓ `character_id`
	- ✓ `book_id`
	- ✓ `character_name`
	- ✓ `quote`

- conversations.jsonl
	- the structure of the conversations
	- every line is a JSON object that contains a conversation chain, which consists of:
		- ✓ `conversation`: `[[character name 1, character id 1, quote], ..., [character name n, quote]]`. 
		- ✓ `book_id` of the book in which the conversation occurred
		- ✓ `book_title`  of the book in which the conversation occurred
		- ✓ `first_line` where the conversation occurs and the `last_line` where the conversation occurs in the raw text of the book.
- raw_urls.txt
	- the urls from Project Gutenberg

## Details
See report.pdf associated with this dataset.
