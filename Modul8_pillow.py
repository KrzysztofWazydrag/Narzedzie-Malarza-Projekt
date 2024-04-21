# instalujemy biblioteke pip install Pillow

from PIL import Image

im = Image.open('flower.jpg')
thumbnail = im.resize(300, 300)
thumbnail.save('resized.jpg')

# Rozbuduj program z poprzedniego zadania(Modul8_filesystem.py) w taki sposób aby obok folderu photos
# pojawił się nowy folder np.resized odtwarzający całą pozostałą ścieżkę do przeskalowanych plików.

#Dla przykładu:
# pystart_code\photos\sample\leaves.jpg
#przeskaluj do pożądanego rozmiaru i umieść w:
# pystart_code\resized\photos\sample\leaves.jpg
from PIL import Image
import argparse
from os import walk, path, makedirs
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='Find Files',
    description='Find and resize files',
    epilog='Author: Kacper Sieradziński'
)
parser.add_argument('--dir')
parser.add_argument('--extension')
arguments = parser.parse_args()

for photo_path, _ , photos in walk(arguments.dir):
    for photo in photos:
        source = Path(f'{photo_path}\\{photo}')
        if source.suffix == '.jpg':
            im = Image.open(source.absolute())
            thumbnail = im.resize(300, 300)
            if not path exists(f'resized\\{photo_path}'):
                makedirs(f'resized\\{photo_path}')

            thumbnail.save(f'resized\\{photo_path}\\{photo}')

#Ten kod jest dość jasny w swoim celu - znajduje pliki w podanym katalogu, zmniejsza zdjęcia w formacie JPG do rozmiaru 300x300 pikseli i zapisuje je w nowym katalogu.
#
# from PIL import Image: Importuje klasę Image z biblioteki PIL (Python Imaging Library), która umożliwia manipulowanie obrazami.
# import argparse: Importuje moduł argparse, który umożliwia analizowanie argumentów wiersza poleceń.
# from os import walk, path, makedirs: Importuje funkcje z modułu os, które są potrzebne do pracy z systemem plików - walk do przechodzenia przez katalogi, path do operacji na ścieżkach i makedirs do tworzenia katalogów.
# from pathlib import Path: Importuje klasę Path z modułu pathlib, który umożliwia operacje na ścieżkach.
# parser = argparse.ArgumentParser(...): Tworzy parser argumentów wiersza poleceń. Określa nazwę programu, opisuje jego działanie i podaje autora.
# parser.add_argument('--dir'): Definiuje argument --dir, który będzie używany do przekazania ścieżki do katalogu z plikami.
# parser.add_argument('--extension'): Definiuje argument --extension, który będzie używany do przekazania rozszerzenia plików, ale nie jest wykorzystywany w dalszej części kodu.
# arguments = parser.parse_args(): Parsuje argumenty przekazane do programu i przypisuje je do zmiennej arguments.
# for photo_path, _ , photos in walk(arguments.dir): Przechodzi przez wszystkie pliki w katalogu podanym jako argument --dir i przypisuje ścieżkę katalogu oraz listę plików do zmiennych photo_path i photos.
# for photo in photos:: Przechodzi przez każdy plik w katalogu.
# source = Path(f'{photo_path}\\{photo}'): Tworzy obiekt ścieżki dla każdego pliku.
# if source.suffix == '.jpg':: Sprawdza, czy rozszerzenie pliku to .jpg.
# im = Image.open(source.absolute()): Otwiera obrazek używając biblioteki PIL.
# thumbnail = im.resize(300, 300): Zmienia rozmiar obrazka na 300x300 pikseli.
# if not path.exists(f'resized\\{photo_path}'):: Sprawdza, czy katalog docelowy dla zmniejszonych obrazków istnieje; jeśli nie, tworzy go.
# thumbnail.save(f'resized\\{photo_path}\\{photo}'): Zapisuje zmniejszony obrazek w katalogu docelowym, zachowując jego oryginalną nazwę.





