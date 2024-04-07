# Korzystając z API dostarczonego przez serwis wolnelektury pobierz wszystkie
# dzieła konkretnego autora. Imie i nazwisko autora powinno zostać przekazane
# jako odpowiedz na pytanie uzytkownika. Zapisz wynik do pliku o nazwie:
# imie-nazwisko-autora.json

import requests

def get_authors_slug(author_name: str) -> str:
    author_request = requests.get('https://wolnelektury.pl/api/authors/')
    for author in author_request.json():
        if author_name == author['name']:
            return author['slug']


authors_slug = get_authors_slug(
    input('Podaj imię i nazwisko autora: ')
)
if authors_slug is not None:
    request = requests.get(f'https://wolnelektury.pl/api/authors/{authors_slug}/books')
    for book in request.json():
        print(book.get('title'))
