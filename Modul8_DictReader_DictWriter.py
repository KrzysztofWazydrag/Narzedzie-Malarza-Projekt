import csv

#

# with open ('orders.csv', mode='w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter= ';', quotechar = '"' )
#     writer.writerow([4,'Kacper','Sieradziński'])

# DictReader uzywamy jesli pierwszy wiersz pliku jest naglowkiem np typ, data, imie, nazwisko
# i tylko wtedy kiedy kolumny mają unikatowe nazwy
# with open ('kocur.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter= ';', quotechar = '"' )
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# Można też zapisywać do pliku csv
with open ('orders2.csv', mode= 'w', newline='') as csvfile2:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writerow({'first_name':'Władek', 'last_name': 'Bizneszczok'})