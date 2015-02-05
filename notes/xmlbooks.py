import xml.etree.ElementTree

catalog = xml.etree.ElementTree.parse('notes/books.xml')

# List the titles of all the books in the catalog
for elem in catalog.findall('book/title'):
    print elem.text

# Show the prices of all the computer books
for book in catalog.findall('book'):
    if book.find('genre').text == 'Computer':
        print book.find('price').text

# List the entire catalog
# with book tag and
# with the ID attributes
# and list all of the sub-elements
for book in catalog.findall('book'):
    print book.tag
    print book.get('id')
    print '------------'
    for field in book:
        print field.tag, '-->', field.text
    print



    


