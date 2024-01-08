number1 = int(input('Podaj pierwszą liczbę: '))

numbers = [number1]

while True:
    try:
        number2 = int(input('Podaj liczbę wyższą niż poprzednia: '))
        if number2 > numbers[-1]:
            numbers.append(number2)
        else:
            print('Ta liczba nie jest wyższa niż poprzednia')
            break
    except ValueError:
        print("To nie jest liczba całkowita.")

average = sum(numbers)/len(numbers)
print(f'Średnia wprowadzonych dotyczas liczb wynosi: {average}')