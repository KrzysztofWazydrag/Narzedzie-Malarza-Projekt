import csv
from datetime import datetime
import matplotlib.pyplot as plt

statistics = {}

with open ('operacje.csv', encoding='utf8', newline='') as file:
    columns = ['data','rodzaj operacji','opis operacji','kwota operacji']
    reader = csv.DictReader(file)
    for row in reader:
        operation_date = datetime.strptime(row['data'], '%Y-%m-%d')
        if operation_date.strftime('%B') not in statistics:
            statistics[operation_date.strftime('%B')] = {
                'total':0,
                'income_quantity':0,
                'expense_quantity':0
            }

        if row['rodzaj operacji'] == 'przychód':
            statistics[operation_date.strftime('%B')]['total'] += float(row['kwota operacji'])
            statistics[operation_date.strftime('%B')]['income_quantity'] += 1
        else:
            statistics[operation_date.strftime('%B')]['total'] -= float(row['kwota operacji'])
            statistics[operation_date.strftime('%B')]['expense_quantity'] += 1

fix, ax = plt.subplots()
months = list(statistics.keys())
totals = []
number_of_operations = []
for month, data in statistics.items():
    totals.append(data['total'])
    number_of_operations.append(data['income_quantity'] + data['expense_quantity'])

ax.bar(months,totals)
plt.savefig('podsumowanie.png')

fig, ax = plt.subplots()
ax.bar(months, number_of_operations)
plt.savefig('ilosc operacji.png')