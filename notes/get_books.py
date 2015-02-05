'Demonstrate how to parse JSON'

import json

with open('notes/books.json') as f:
    catalog = json.load(f)
    
for bookid in catalog:
    book = catalog[bookid]
    if book['genre'] == 'Computer':
        print book['price'], book['title']
