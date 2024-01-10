import math

list1 = (8, 7, 0, 7, 1, 6, 1, 8, 6, 9, 7)
list2 = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1)
if len(list1) == 11:
    print("Twój pesel ma odpowiednią ilość znaków")

result = [a * b for a, b in zip(list1, list2)]
list3 = sum(result)
print(list3)

new = str(list3)
if new.endswith('0'):
    print('jest okej')



