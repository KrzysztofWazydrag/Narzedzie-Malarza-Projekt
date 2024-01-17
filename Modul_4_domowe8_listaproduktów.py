# Przygotuj słownik zawierajacy produkty.
# zapytaj uzytkownika ktory produkt chce dodac do koszyka, a nastepnie w jakiej ilosci
#pytaj dopoki nie pojawi sie 'podsumuj'
#wartosc zamowienia mozesz przechowywac w pojedynczej zmiennej lub posiadac listę(dla chetnych) produktow
# lub słownikow jesli chcesz wyswietlic podsumowanie


products = {
    'doniczka': 15,
    'konewka': 20,
    'grabie': 12,
    'szpadel': 18,
    'kosiarka': 350,
    'łopata': 22,
    'siekierka': 28,
    'młotek': 12,
    'wiadro': 8
}

print('Produkty w sklepie: ')
for name, price in products.items():
    print(f' - {name}, cena: {price} zł')

cart = {}
while (name:=input('Podaj nazwę produktu: ')) != 'podsumuj':
    cart[name] = cart.get(name, 0) + int(input('Ile sztuk produktu chcesz zakupić? '))

total = 0
print('Produkty do opłacenia: ')
for name, quantity in cart.items():
    total += products[name] * quantity
    print(f' - {name}, wartość: {products[name] * quantity} zł')

print('---' *10)
print(f'Łączna wartość : {total}')