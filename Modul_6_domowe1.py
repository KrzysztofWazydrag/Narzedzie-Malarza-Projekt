#Przygotuj funkcję, która będzie odbierała argumenty w postaci:
#group them(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green")
#W odpowiedzi funkcja powinna wyświetlić(w osobnych wierszach)
#Wall is red \n Tomato is red \n Light is yellow itd.


def group_them(**kwargs):
    output = []
    for key, value in kwargs.items():
        output.append(f'{key.title()} is {value}')

    return '\n'.join(output)


def test_group_them():
    assert group_them() == ''
    assert group_them(python='super') == 'Python is super'
    assert group_them(wall='red', tomato='red') == 'Wall is red\nTomato is red'

if __name__ == '__main__':
    print(group_them(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green"))
    print(group_them(banana="yellow", python="gites", java="nice", lemon="yellow", grass="green"))