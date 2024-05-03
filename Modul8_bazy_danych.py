import sqlite3

with open ('library.db') as connection:
    pass


#book_id - nazwa kolumny, INTEGER - liczba calkowita,
# PRIMARY KEY - klucz główny, gdy tworzymy tabele powinnismy miec jedną kolumnę która bedzie reprezentowala ten rekord,
#bedzie unikatowa dla kazdego rekordu np jesli masz uzytkownikow to email moglby byc kluczem glownym,
# czesto kluczem glownym jest liczba od 1 do tylu ile mamy rekordow w bazie danych(nie zawsze)
# autoincrement powoduje ze jak dodasz rekord to przypisze mu odpowiednią liczbę i ją zapamieta
# np masz 3 ksiazki, usuwasz 2 i dodajesz potem 1(jedną) to zostają numery 1 i 4 i po dodaniu kolejnych bedzie 5,6 itd po kolei
# varchar tzn zmienna dlugosc kolumny z max 100 znaków
# unique - nie moze sie powtarzac ta nazwa
# not null nie moze byc pusta
CREATE TABLE books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) UNIQUE NOT NULL,
    author VARCHAR(100)
)

INSERT INTO
    books(title, author)
VALUES
('W pustyni i w puszczy', 'Henryk Sienkiewicz')