# Zadanie 2: Napisz program, który będzie konwertował różne jednostki masy na podstawie wyboru użytkownika.
# Użytkownik powienien mieć możliwość konwersji między kilogramami, funtami i uncjami.
# Przelicznik jest 1 kilogram = 35.274 uncji oraz 1 kilogram = 2.20462 funtów.

kg_oz = 34.274
kg_lb = 2.20462
value = float(input('Podaj wartość do zmiany: '))
print('1. Zamiana kilogramów na uncje.')
print('2. Zamiana uncji na kilogramy.')
print('3. Zamiana kilogramów na funty.')
print('4. Zamiana funtów na kilogramy.')





match int(input('Jakiej zamiany chcesz dokonać? ')):
    case 1: result = value * kg_oz
    case 2: result = value / kg_oz
    case 3: result = value * kg_lb
    case 4: result = value / kg_lb

print(f'Wartość przed zmianą: {value}, po zmianie {result:.2f}.')
