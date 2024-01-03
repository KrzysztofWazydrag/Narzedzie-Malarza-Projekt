from random import choice

capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Argentyna': 'Buenos Aires',
    'Brazylia': 'Brasilia',
    'USA':'Waszyngton',
    'Słowacja':'Bratysława',
    'Czechy': 'Praga',
    'Węgry': 'Budapeszt',
    'Macedonia':'Skopje',
    'Francja': 'Paryż',
    'Holandia': 'Amsterdam',
    'Hiszpania': 'Madryt',
    'Łotwa': 'Ryga',
    'Litwa': 'Wilno',
    'Dania': 'Kopenhaga',
    'Bułgaria': 'Sofia',
    'Chorwacja': 'Zagrzeb',
    'Belgia': 'Bruksela',
    'Albania': 'Tirana',
    'Norwegia': 'Oslo',
    'Jamajka': 'Kingston',
    'Kanada': 'Ottawa'
}




correct_answers = 0
for a in range(3):
    selected_country = choice(list(capitals.keys()))
    answer = input(f'Podaj stolicę {selected_country}: ')
    if answer == capitals[selected_country]:
        print('Odpowiedź prawidłowa')
        correct_answers += 1
    else:
        print('Spróbuj jeszcze raz')

if correct_answers == 3:
    print("Brawo, bezbłędnie! Gratuluję!")
elif correct_answers == 2:
    print('Tylko 1 błąd, nieźle!')
elif correct_answers == 1:
    print('Jeden punkt na otarcie łez :) ')
else:
    print('Następnym razem będzie lepiej')