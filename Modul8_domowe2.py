# Znajdź sposób listowania plików w katalogu, a następnie napisz program, który odszuka wszystkie
# pliki tekstowe w wybranym przez Ciebie folderze i do nowego pliku o nazwie scalone.txt
# wstawi wynik jakim będą połączone te pliki.

import os
from pathlib import Path

# Ścieżka do folderu z plikami tekstowymi
folder_path = 'sciezka/do/twojego/folderu'

# Tworzenie obiektu Path dla folderu
folder = Path(folder_path)

# Znalezienie wszystkich plików tekstowych w folderze
text_files = folder.glob('*.txt')

# Połączenie zawartości wszystkich plików tekstowych w jeden plik scalone.txt
with open('venv/scalone.txt', 'w', encoding='utf-8') as outfile:
    for file in text_files:
        with open(file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content)
            outfile.write('\n')  # Dodanie nowej linii między plikami (opcjonalnie)

print(f'Połączono {len(list(folder.glob("*.txt")))} plików tekstowych do scalone.txt')