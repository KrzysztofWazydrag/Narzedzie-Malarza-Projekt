#Utwórz bazę danych o nazwie test_ip w bazie powinna znaleźć się tabela
#ip_to_check, która powinna zawierać jedną kolumnę zawierającą tylko adresy
#IP do sprawdzenia oraz drugą tabelę log, która będzie przechowywała datę sprawdzenia,
#oraz informację o sukcesie lub porażce

#Skrypt powinien odpytywać wszystkie adresy IP co 5 minut - skorzystaj z biblioteki time, funkcji sleep
#i czeka 5* 60 sekund. Odpytywanie możesz zrealizować za pomocą polecenia ping.

from time import sleep
import sqlite3
from sys import argv
import subprocess

def get_ips(db_connection):
    cursor = db_connection.cursor()
    res = cursor.execute('SELECT ip FROM ip')

    return res

def save_status(db_connection, ip:str, is_up:bool):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO log(ip, is_up) VALUES(?, ?)',(
        ip,
        int(is_up)
    ))


def check_if_is_up(ip:str) ->bool:
    output = subprocess.run(['ping', ip], capture_output=True, shell=True)
    if 'could not' in output.stdout.decode('utf8').lower():
        return False

    return True
def initialize(db_connection):
    sqls = ['''CREATE TABLE ip_to_check(
        ip TEXT
    )''', '''CREATE TABLE log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_up INTEGER
    )''']
    cursor = db_connection.cursor()

    for sql in sqls:
        cursor.execute(sql)

    db_connection.commit()

def main():
    with sqlite3.connect('ip_to_check.db') as connection:
        if len(argv) == 2 and argv[1] == 'setup':
            initialize(connection)

        for ip, in get_ips(connection):
            save_status(connection, ip, check_if_is_up(ip))

while True:
    main()
    sleep(5 * 60)
