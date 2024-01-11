while True:
    value1 = int(input('Wartość 1: '))
    value2 = int(input('Wartość 2: '))
    action = input('Jakie obliczenie cię interesuje: ?')

    match action:
        case 'dodawanie': result = value1 + value2
        case 'odejmowanie': result = value1 - value2
        case 'mnozenie' | 'mnozenie': result = value1 * value2
        case 'dzielenie': result = value1 / value2
        case 'koniec': break
        case _:
            print('Nie wiem co mam zrobić.')
            result = 'error'

    print(f'Wynik operacji wynosi {result}')
    input()

