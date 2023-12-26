from math import ceil

print('Witam w narzędziu Malarza!!! Pomogę ci obliczyć ilość potrzebnej farby oraz gruntu :) ')


#Pytamy użytkownika o ilość ścian.
walls_amount = int(input('Ile jest ścian do pomalowania? '))
previous_height = 2.5
total_area = 0

for counter in range(walls_amount):
    width = float(input(f'Podaj szerokość ściany nr {counter + 1} w metrach: '))
    height = input(f'Podaj wysokość ściany nr {counter + 1} w metrach: ')


    if height == '':
        height = previous_height
    else:
        height = float(height)
        previous_height = height


# Obliczenie powierzchni do pomalowania
    total_area += (height * width)

print(f"Powierzchnia do pomalowania wynosi {total_area}")

#pytanie uzytkownika o ilość warstw
grunt = int(input('Prosze podac ilosc warstw gruntu: '))
farba = int(input('Prosze podac ilosc warstw farby: '))


# obliczenie:  wydajność gruntu 5mkw = 1 litr/ wydajność farby 13mkw = 1 litr
grunt_required = ceil(total_area * grunt / 5)
farba_required = ceil(total_area * farba / 13)

print(f'Potrzebujesz {grunt_required} litrów gruntu')
print(f'Potrzebujesz {farba_required} litrów farby')

#Koniec projektu

