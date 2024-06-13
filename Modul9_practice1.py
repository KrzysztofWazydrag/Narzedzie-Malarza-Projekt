# Zaimplementuj klasę Circle, która w metodzie init powinna odebrać promień koła.
# Klasa ta powinna posiadać dwie metody liczące pole, a także obwód koła. Pamiętaj o testach
#
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius: int):
#         self.radius = radius
#
# # obliczamy obwód koła
#     def get_circumference(self) -> float:
#         return self.radius * 2 * pi
#
# # obliczamy pole koła
#     def get_field(self) -> float:
#         self.radius ** 2 * pi
#
#
# def test_circle_calculations():
#     circle = Circle(5)
#     field = circle.get_field()
#     circumference = circle.get_circumference()
#
#     assert 78.5 < (field) < 78.6
#     assert 31.4 < (circumference) < 31.5
#
#
#
# if __name__ == '__main__':
#     radius = int(input('Podaj promień: '))
#     circle = Circle(radius)
#     print('Pole koła wynosi', circle.get_field())
#     print('Obwód koła wynosi', circle.get_circumference())


# Przygotuj klasę Car, która powinna przechowywać nazwę samochodu oraz jego cenę i maksymalną prędkość.
# Zapytaj użytkownika o 5 samochodów, a następnie wyświetl je na ekranie.

class Car:
    def __init__(self, brand, cost, max_speed):
        self.brand = brand
        self.cost = cost
        self.max_speed = max_speed

    def __str__(self):
        return (f'Car(brand={self.brand}, cost={self.cost}, max speed={self.max_speed}')



def get_five_cars():
    cars = []
    for counter in range(1, 6):
        print(f'Entering details for car number {counter}:')
        brand = input('Car Brand: ')
        cost = float(input('Car Cost: '))
        max_speed = float(input('Max Speed: '))
        car = Car(brand, cost, max_speed)
        cars.append(car)
    return cars

def main():
    cars = get_five_cars()
    print('\nList of entered cars:')
    for counting, car in enumerate(cars, start=1):
        print(f'{counting}.{car}')


#main function
if __name__ == '__main__':
    main()



