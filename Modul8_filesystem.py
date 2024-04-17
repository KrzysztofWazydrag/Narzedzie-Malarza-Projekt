import argparse
from os import walk
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='Find Files',
    description='Find and resize files',
    epilog='Author: Kacper Sieradziński'
)
parser.add_argument('--dir')
parser.add_argument('--extension')
arguments = parser.parse_args()

for path, _ , photos in walk(arguments.dir):
    for photo in photos:
        source = Path(f'{path}\\{photo}')
        if source.suffix == '.jpg':
            print(source.absolute())

# Ten kod to mały program w Pythonie, który pomaga znaleźć pliki w określonym katalogu i wyświetla ich ścieżki.
# Oto jego wyjaśnienie krok po kroku:
# import argparse: Importuje moduł argparse, który pozwala nam łatwo przetwarzać argumenty przekazywane do programu z wiersza poleceń.
# from os import walk: Importuje funkcję walk z modułu os, która pomaga w przechodzeniu przez katalogi i pliki w drzewie katalogów.
# from pathlib import Path: Importuje klasę Path z modułu pathlib, która dostarcza wygodne sposoby manipulowania ścieżkami.
# Tworzymy parser argumentów używając ArgumentParser z argparse.
# Przekazujemy kilka opcji, takich jak prog (nazwa programu), description (opis programu) i epilog (dodatkowe informacje na końcu).
# Dodajemy dwa argumenty do parsera za pomocą add_argument. Oba argumenty są opcjonalne (--dir i --extension), co oznacza,
# że użytkownik może je podać albo nie.
# arguments = parser.parse_args(): Parsujemy argumenty przekazane do programu i zapisujemy je do zmiennej arguments.
# Rozpoczynamy pętlę for, która przechodzi przez katalogi i pliki w podanym przez użytkownika katalogu (arguments.dir) za pomocą funkcji walk.
# Wewnętrzna pętla for przechodzi przez wszystkie pliki w bieżącym katalogu.
# Tworzymy obiekt Path dla każdego znalezionego pliku, łącząc ścieżkę do katalogu z nazwą pliku.
# Sprawdzamy, czy plik ma rozszerzenie ".jpg" za pomocą source.suffix. Jeśli tak, drukujemy jego ścieżkę bezwzględną (source.absolute()).
# To wszystko! Program ten pozwala użytkownikowi podać katalog i opcjonalne rozszerzenie pliku, a następnie znajduje i wyświetla ścieżki do plików z danym rozszerzeniem w podanym katalogu.'''