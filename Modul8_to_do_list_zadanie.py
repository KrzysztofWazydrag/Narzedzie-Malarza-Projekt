import sqlite3
from sys import argv
def setup():
    with sqlite3.connect('todo.db') as connection:
        sql = '''CREATE TABLE books(
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(100) UNIQUE NOT NULL,
            is_done INTEGER DEFAULT 0    
        )'''

    # utworzylismy zapytanie tworzące naszą tabelę, małe litery to wymyslone zmienne a duze pochodza z sqla
    # cursor - obiekt ktory sluzy do wykonywania zapytania

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
# kod powyżej tworzy bazę danych

if len(argv) == 2 and argv[1] == 'setup':
    setup()

with sqlite3.connect('todo.db') as connection:
    cursor = connection.cursor()
    for todo in cursor.execute('SELECT * FROM todos WHERE is_done=0'):
        print(todo)

    print('Co chcesz zrobić?')
    print('0 - Dodaj nowe zadanie')
    print('1 - Ustaw zadanie jako zrealizowane')
    value = input('Którą czynność chcesz wykonać? ')
    if value == '0':
        title = input('Co masz do zrobienia?')
        cursor.execute('INSERT INTO todos(title) VALUES(?)', (title,))
        connection.commit()
    elif value == '1':
        todo_id = input('Podaj ID zadania, które zrobiłeś: ')
        cursor.execute(('UPDATE todos SET is_done=1WHERE todo_id=?)), (todo_id)
                        connection commit(_)
    else:
        print('Dokonałeś nieprawidłowego wyboru')