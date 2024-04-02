from requests import get

# MOJA WERSJA
# url = 'https://danepubliczne.imgw.pl/api/data/synop'
#
# towns = 'Tarnow'
#
# response = get(url)
# data = response.json()
#
# for row in data:
#     print(row['stacja'], row['temperatura'])


#WERSJA KACPRA
response = get('https://danepubliczne.imgw.pl/api/data/synop')

for row in response.json():
    if row['stacja'] == 'Kraków' or row['stacja'] == 'Tarnów':
        print(row['cisnienie'], row['temperatura'])