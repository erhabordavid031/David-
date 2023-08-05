'''
Library Management System
@author: David Ekinadoese

'''


actions = '\n'.join([
    '1. Register a book',
    '2. Borrow a Book',
    '3. List Books on shelve'
])

heading:str = f'''
Welcome to the Library Management System.
This is a Command-Line Application.
(C) 2023 David Ekinadoese

Actions
=======
{actions}
'''
import json
with open('books.json', 'r') as f:
    books = json.loads(f.read())

print(heading)
action = input('>>> ')
if action == '1':
    # Register a book
    book_title = input('Book Title: ')
    book_author = input('Book Author: ')
    book_pub_year = input('Pub Year: ')
    book_ISBN = input('ISBN: ')
    CUN = input('Call Number: ')
    copies = int(input('Number of Copies: '))
    book = {
        'Title': book_title,
        'Author': book_author,
        'Pub Year': book_pub_year,
        'ISBN': book_ISBN,
        'Call Number': CUN,
        'Number of Copies': copies
    }
    books.append(book)
    with open('books.json', 'w') as f:
        json.dump(books, f)
    print(f'Book registered successfully wil call number: {book["Call Number"]}')

if action == '2':
    CUN = input('Call Number: ')
    for book in books:
        if book['Call Number'] == CUN:
            selected_book = book
        print(f'{ selected_book["Title"] } borrowed successfully')

if action == '3':
    print('Title\t  |  Author |  Pub Year  |  ISBN  |  Call Number  |  Number of Copies')
    print('-'*80)
    for book in books:
        print(f'{book["Title"]}\t\t  |  {book["Author"]}\t\t  |  {book["Pub Year"]}\t\t  |  {book["ISBN"]}\t\t  |  {book["Call Number"]}\t\t  |  {book["Number of Copies"]}')

        


          