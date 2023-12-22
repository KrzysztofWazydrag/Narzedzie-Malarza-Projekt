print('Witam w narzędziu Malarza!!! Pomogę ci obliczyć ilość potrzebnej farby oraz gruntu :) ')


#Pytamy użytkownika o ilość ścian.
walls_amount = int(input('Ile jest ścian do pomalowania? '))
repeat_height = input('Jeśli chcesz przyjąć poprzednią wysokość to wciśnij "Enter": ')

#Pytamy użytkownika o ilość ścian.
width = int(input('Podaj szerokość ściany w metrach: '))
height = int(input('Podaj wysokość ściany w metrach: '))

# Obliczenie powierzchni do pomalowania
total_walls = walls_amount * (width*height)

print(f"Powierzchnia do pomalowania wynosi {total_walls}")

#pytanie uzytkownika o ilość warstw
grunt = int(input('Prosze podac ilosc warstw gruntu: '))
farba = int(input('Prosze podac ilosc warstw farby: '))


# obliczenie:  wydajność gruntu 5mkw = 1 litr
grunt_required = (total_walls/5) * grunt
farba_required = (total_walls/5) * farba

print(f'Potrzebujesz {grunt_required:.2f} litrów gruntu')
print(f'Potrzebujesz {farba_required:.2f} litrów farby')



