# Odczytaj zawartość pliku logi.txt i policz ile czasu poszczegolnie uzytkownicy spedzili w aplikacji.
# Plik załączony pod filmem.

from datetime import datetime

time_spent = {}
last_seen = {}

with open('logi.txt', encoding='utf8') as file:
    for line in file:
        row = line.strip().split(';')
        if len(row) != 3:
            continue

        created_at, username, action = row
        created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')

        if action == 'login':
            last_seen[username] = created_at

        if action == 'logout':
            delta = created_at - last_seen[username]
            time_spent[username] = time_spent.get(username, 0) + delta.seconds

for username, spent in time_spent.items():
    print(f'Użytkownik {username} spędził na stronie {spent} s.')

