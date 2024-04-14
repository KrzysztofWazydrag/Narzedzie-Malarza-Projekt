import csv
data = [
    {'Name':'Hennessey Venom F5', 'time_to_100':2.6, 'speed_record':484},
    {'Name':'SSC Tuatara', 'time_to_100':2.5, 'speed_record':460},
    {'Name':'Koeningsegg Agera RS', 'time_to_100':3.1, 'speed_record':457},
    {'Name':'Koeningsegg One 1', 'time_to_100':2.6, 'speed_record':450},
    {

    }
]

# zapis do pliku csv

with open('fast_cars.csv', mode='w') as csvfile:
    header = ['Name','time_to_100','speed_record']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# odczyt tego pliku


