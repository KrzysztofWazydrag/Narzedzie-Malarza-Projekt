# 1. Poproś użytkownika o datę rozpoczęcia, datę zakończenia, a także o jego dniówkę.
# W odpowiedzi powinna wyświetlić się informacja ile użytkownik zarobi.
# 2. Spróbuj wyświetlić za pomocą pętli wszystkie dni pomiędzy dwiema datami z poprzedniego zadania.
# 3. Policz podwójnie wynagrodzenie pracownika za pracę w soboty i niedziele.


from datetime import datetime, timedelta

date_start = datetime.strptime(input('Proszę podać datę rozpoczęcia dd.mm.rrrr: '), '%d.%m.%Y')
date_end = datetime.strptime(input('Proszę podać datę rozpoczęcia dd.mm.rrrr: '), '%d.%m.%Y')
rate = float(input('Proszę podać datę stawkę dzienną: '))

diff = date_end - date_start
salary = (diff.days + 1) * rate

print(f'Do wypłaty {salary} PLN')

while date_start <= date_end:
    if date_start.strftime('%a') in ['Sat', 'Sun']:
        salary += rate

    print(date_start.strftime('%a %d.%m.%Y'))
    date_start += timedelta(days=1)

print(f'Do wypłaty {salary} PLN')






