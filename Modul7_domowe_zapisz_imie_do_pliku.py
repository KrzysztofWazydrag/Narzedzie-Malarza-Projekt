# Napisz program, który pyta użytkownika o jego imie i nazwisko
# oraz zapisuje te informacje w pliku tekstowym

first_name = input('Podaj imie: ')
last_name = input('Podaj nazwisko: ')

with open('full_name.txt', 'a', encoding='utf8') as file:
    file.write(f'{first_name} {last_name}\n')