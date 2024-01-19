#Zadanie 11: zapytaj użytkownika o dwa wyrażenia, a nastepnie wyswietl wszystkie znaki wspolne
#dla obu tych wyrazen. np. sala i balkon: powinno wyswietlic a oraz l

sentence1 = input('Podaj slowo: ')
sentence2 = input('Podaj drugie slowo: ')

wspolne = []

# Iteracja przez każdą literę w pierwszym wyrażeniu
for litera in sentence1:
    # Sprawdzenie, czy litera istnieje w drugim wyrażeniu i nie jest już w liście wspólnych liter
    if litera in sentence2 and litera not in wspolne:
        wspolne.append(litera)

# Wyświetlenie wspólnych liter
if wspolne:
    print("Wspólne litery: " + ", ".join(wspolne))
else:
    print("Brak wspólnych liter.")