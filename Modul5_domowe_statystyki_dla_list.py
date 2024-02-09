#Przygotuj funkcję, która dla dowolnej listy zwróci słownik zawierający:
#total = ilosc elementów
#mean = średnią elementów
#max = największą wartość
#min = najmniejszą wartość


def get_dictionary(elements:list) ->dict:

    return  {
        'total': len(elements),
        'mean': sum(elements) / len(elements),
        'max':max(elements),
        'min':min(elements)
    }

print(get_dictionary([1,2,3,4,5,6,7,8,9]))