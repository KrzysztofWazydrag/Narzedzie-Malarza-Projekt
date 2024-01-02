countries = [
    {'country': 'Polska', 'capital': 'Warszawa', 'official_language': 'polski'},
    {'country': 'Niemcy', 'capital': 'Berlin', 'official_language': 'niemiecki'},
    {'country': 'Czechy', 'capital': 'Praga', 'official_language': 'czeski'},
    {'country': 'Słowacja', 'capital': 'Bratysława', 'official_language': 'słowacki'},
    {'country': 'Słowenia', 'capital': 'Lublana', 'official_language': 'słoweński'}
]
print(countries)


countries.append({
    'country': input('Podaj nazwę kraju: '),
    'capital': input('Podaj stolicę tego kraju: '),
    'official_language' : input(f'Podaj język urzędowy tego kraju: ')
})

for country in countries:
    for column, value in country.items():
        print(f'{column}: {value}')

    print('---' * 10)