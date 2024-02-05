def power(number):
    if number == 0:
        return 1

    return number * power(number -1)

#dodatkowo petla for moze wszystkie wypisac i wyliczyc
for n in range(11):
    print(n, power(n))

print('---'*10)

print(power(3))