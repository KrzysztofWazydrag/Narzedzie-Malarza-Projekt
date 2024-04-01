from json import load, dump

operation = input('Co chcesz zrobić? [d] Dodaj wydatek, [w] Wypisz wszystkie: ')

with open('wydatki.json') as file:
    expenses = load(file)

if operation == 'd':
    title = input('Czego dotyczy wydatek? ')
    value = float(input('Jaka kwota została wydana? '))
    expenses.append({
        'title': title,
        'value': value
    })
    with open('wydatki.json', 'w') as file:
        dump(expenses, file)

elif operation == 'w':
    total = 0
    for expense in expenses:
        total += expense.get('value')
        # print(expense['title'], expense['value']) - pierwsza wersja też prawidłowa, druga jest z get i nawiasami okrągłymi
        print(expense.get('title'), expense.get('value'))
        print('Łączna wartość wydatków to', total)