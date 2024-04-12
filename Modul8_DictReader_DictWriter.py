import csv

#

# with open ('orders.csv', mode='w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter= ';', quotechar = '"' )
#     writer.writerow([4,'Kacper','Sieradziński'])

# DictReader uzywamy jesli pierwszy wiersz pliku jest naglowkiem np typ, data, imie, nazwisko

with open ('kocur.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter= ';', quotechar = '"' )
    for row in reader:
        print(row['first_name'], row['last_name'])