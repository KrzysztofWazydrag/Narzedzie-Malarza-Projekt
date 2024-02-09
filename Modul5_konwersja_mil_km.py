# Przygotuj funkcję, której zadaniem będzie konwersja jednostek: mil na kilometry
# i drugą wykonującą konwersję kilometrów na mile
from math import ceil


# 1 mila = 1,609344 kilometra

def get_km (distance:float, mile = 1.609344) ->float:
    return distance * mile


def get_mile (distance:float, mile = 1.609344) ->float:
    return distance / mile

print(ceil(get_km(10)))
print(ceil(get_mile(10)))