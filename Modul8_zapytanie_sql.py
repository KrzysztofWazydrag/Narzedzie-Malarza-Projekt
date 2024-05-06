import sqlite3

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    title = input('Tytuł: ')
    author = input('Autor: ')
    cursor.execute('insert into books VALUES (null, ?, ?)', (title, author))
    connection.commit()