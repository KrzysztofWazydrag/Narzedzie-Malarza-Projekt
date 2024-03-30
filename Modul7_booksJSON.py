from json import load, dump

new_author = "Witold Gombrowicz"
new_title = "Ferdydurke"

#otwieramy plik pierwszy raz zeby go odczytac
with open('books.json') as file:
    books = load(file)

for book in books:
    print('Tytuł', book.get('title'))
    print('Autor:', book.get('author'))
    print('---' * 10)

#otwieramy plik drugi raz zeby do niego dodac dodatkowa ksiazke i dodajemy "dump" do importu
with open('books.json', 'w') as file:
    books.append({
        'title': new_title,
        'author': new_author})
    dump(books, file)