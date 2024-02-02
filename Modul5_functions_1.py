from math import ceil

def get_divisors (number, start=2):
    divisors = set()
    for divisor in range(start, ceil(number / 2) + 1):
        if number % divisor == 0:
            divisors.add(divisor)

    return divisors



def get_common_divisors(number1, number2, start=1):
    divisors1 = get_divisors(number1, start)
    divisors2 = get_divisors(number2, start)

    return divisors1 & divisors2

number1 = int(input('Liczba1: '))
number2 = int(input('Liczba2: '))
minimum = int(input('Start: '))

print(number1, get_divisors(number1))
print(number2, get_divisors(number2))


print(get_common_divisors(number1, number2, minimum))






# def multiply(a,b=2):
#     return a * b
#
# print(multiply(2,5))