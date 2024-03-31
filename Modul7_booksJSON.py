from json import load, dump

#otwieramy plik pierwszy raz zeby go odczytac
with open('books.json') as file:
    books = load(file)
    for book in books:
        print('Tytuł', book.get('title'))
        print('Autor:', book.get('author'))
        print('---' * 10)


#otwieramy plik drugi raz zeby do niego dodac dodatkowa ksiazke i dodajemy "dump" do importu
with open('books.json', 'w') as file:
    new_author = input('Imię i nazwisko autora: ')
    new_title = input('Podaj tytuł książki: ')
    books.append({
        'title': new_title,
        'author': new_author
    })
    dump(books, file)

