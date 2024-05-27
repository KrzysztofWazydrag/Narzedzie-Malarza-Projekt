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

from requests import get
from datetime import date

def get_weather_for_location(location):
   response = get('https://danepubliczne.imgw.pl/api/data/synop')
   for row in response.json():
       if row['stacja'] == 'Gdańsk' or row['stacja'] == 'Kasprowy Wierch':
           return {'cisnienie':row['cisnienie'], 'temperatura': row['temperatura'] }

def add_weather(connection, location, weather):
