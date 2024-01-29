#Przygoyuj funkcje, która zwróci True albo False, w zaleznosci od tego czy liczba ta jest pierwsza.
from math import ceil, sqrt


def is_prime(number):
    for divider in range(2, ceil(sqrt(number))+1):
        if number % divider == 0:
            return False

    return True

for n in range(1000, 1020):
    print(n, is_prime(n))