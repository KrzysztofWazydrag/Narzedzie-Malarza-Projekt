#Przygotuj program, który przeskanuje katalog pod kątem różnych
#rozszerzeń. Wynikiem powinien być wykres prezentujący te rozszerzenia
#oraz ilość plików. Np. txt: 10, jpg: 3, py: 2
#Dodatkowo: utwórz plik csv o następującej strukturze:
#filetype;quantity
#txt;10
#jpg;3
#py;2

from pathlib import  Path
from os import walk

# for path, dirs, files in walk('source'):     --potrzebujemy tylko file
# żeby pobrać rozszerzenie potrzebujemy zrobić Path na pliku

statistics = {}
for _, _, files in walk('d:/Pystart'):
    for file in files:
        path = Path(file)
        extension = path.suffix.replace('.','')
        statistics.update({extension: statistics.get(extension, 0) +1})

print(statistics)