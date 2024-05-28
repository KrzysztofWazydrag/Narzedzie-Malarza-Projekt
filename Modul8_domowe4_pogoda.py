#Pamiętasz dane pogodowe pobierane z serwisu imgw?
#Przygotuj program o nazwie pogoda.py którego zadaniem będzie pobieranie informacji o pogodzie w konkretnej
#stacji pogodowej i zapisywanie tych informacji w bazie danych. https://www.sqlite.org.datatype3.html
#Interesują nas dane takie jak:
#data pomiaru
#nazwa stacji
#temperatura
#cisnienie
#
#Jezeli dla danego dnia byl juz zarejestrowany pomiar
#to nie powinien byc on dodawany do bazy danych drugi raz.
import sqlite3
from sys import argv
from requests import get
from datetime import date

def get_weather_for_location(location):
   response = get('https://danepubliczne.imgw.pl/api/data/synop')
   for row in response.json():
       if row['stacja'] == location:
           return {'pressure':row['cisnienie'], 'temperature': row['temperatura'] }


#tworzymy tabelę żeby zapisać dane w konkretnym miejscu, connection - polaczenie z bazą danych,
def add_weather(connection, created_at: date, location:str, weather):
    created_at = created_at.strftime('%Y-%m-%d')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO weather(created_at, station, temperature, pressure) VALUES(?, ?, ?, ?)', (
        created_at,
        location,
        weather['temperature'],
        weather['pressure']
    ))

    connection.commit()

def get_weather_for_date_and_location(connection, created_at:date, location:str) -> dict:
    cursor = connection.cursor()
    result = cursor.execute(
        'SELECT * FROM weather WHERE station =? AND created_at=?', (location, created_at.strftime('%Y-%m-%d'))
    )

    return result.fetchone()

#cos co tworzy tabelę
def initialize(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE weather(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    station TEXT,
    temperature REAL,
    pressure REAL
    )''')
    connection.commit()

with sqlite3.connect('weather.db') as connection:
    if len(argv) == 2 and argv[1] == 'setup':
        initialize(connection)

    station = 'Kraków'
    today = date.today()
    row = get_weather_for_date_and_location(connection, today, station)
    if row is None:
        add_weather(connection, today, station, get_weather_for_location(station))