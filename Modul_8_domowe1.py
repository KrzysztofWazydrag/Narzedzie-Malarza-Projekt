#Pytaj użytkownika o nazwy produktów tak długo aż nie napisze 'koniec'
#Zapisz wówczas do pliku o nazwie według wzoru ddmmrrr.txt
#tylko unikatowe nazwy wprowadzonych przez niego produktów

from datetime import datetime

products = set()
while (product_name := input('Podaj nazwę produktu: ')) != 'koniec':
    products.add(product_name)

today = datetime.now()
filename = today.strftime('%d%m%Y') + '.txt'

with open(filename, 'w', encoding='utf8') as file:
    file.write('\n'.join(products))