# gutenberg-conversations
gutenberg-conversations dataset
contents of this README:

	1) brief description
	2) files description
	3) details on the collection procedure
	4) contact


brief description:

This corpus contains a metadata-rich collection of fictional conversations extracted from raw novels of The Gutenberg Project

- 86185 conversational exchanges between pairs of movie characters
- involves 67942 characters from 928 novels
- in total 578213 utterances
- novel metadata not included yet: %TO DO:
	✗ genres
	✗ Goodreads rating
- character metadata not included: %TO DO:
	✗ gender (for all characters)
	✗ position on novel hierarchy


2) files description:

In all files the field separator is ","

- characters_meta.csv
	- info about characters
	- fields:
		✓ character_id
		✓ character_name (after clustering)
		✓ book_id
		✓ book_title
		✗ gender ("_" for unknown cases)
		✗ other traits: position in a hierarchy (but how we determine this hierarchy automatically? or http://learn.lexiconic.net/characters.htm), sentiment, adjectives/adverbs that are most frequent used by those characters, networks of relationships to others?  

- books_quotes.csv
	- contains the actual text of each quote
- fields:
		✓ line_id
		✓ character_id
		✓ book_id
		✓ character_name
		✓ quote

- conversations.jsonl
	- the structure of the conversations
	- every line is a JSON object that contains a conversation chain
		✓ list all character_ids of a characters involved in the conversation and their quotes that make the conversation in chronological order: ’conversation’: [[character name 1, charac- ter id 1, quote], ..., [character name n, quote], ’last line’:y, ’first line’: x] . 

		✓ book_id of the book in which the conversation occurred
		✓ book_title  of the book in which the conversation occurred
		✓ first line where the conversation occurs and the last line where the conversation occurs in the raw text of the book.
- raw_urls.txt
	- the urls from Project Gutenberg

3) details on the collection procedure:
See report.pdf associated with this dataset.

4) contact:

Please email any questions to: sarnthil@gmail.com (Bostan Laura-Ana-Maria)

