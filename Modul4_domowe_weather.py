#stwórz słownik miasta i temperatury po pytaniu uzytkownika

measurements = {}

while (city := input('Podaj nazwę miasta lub "koniec" aby zakończyć: ')) != 'koniec':
    measurements[city] = int(input(f'Podaj temperaturę dla miasta {city}: '))

average = sum(measurements.values()) / len(measurements.values())
print(f'Średnia temperatura wynosi {average:.2f}')

highest_temperature = []
lowest_temperature = []

for city, temperature in measurements.items():
    if temperature == max(measurements.values()):
        highest_temperature.append(city)

    if temperature == min(measurements.values()):
        lowest_temperature.append(city)


print('Najwyższa temperatura', highest_temperature)
print('Najniższa temperatura', lowest_temperature)
