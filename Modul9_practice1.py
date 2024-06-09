# Zaimplementuj klasę Circle, która w metodzie init powinna odebrać promień koła.
# Klasa ta powinna posiadać dwie metody liczące pole, a także obwód koła. Pamiętaj o testach

from math import pi


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

# obliczamy obwód koła
    def get_circumference(self) -> float:
        return self.radius * 2 * pi

# obliczamy pole koła
    def get_field(self) -> float:
        self.radius ** 2 * pi


def test circle_calculations():
    circle = Circle(5)
    field = circle.get_field()
    circumference = circle.get_circumference()

    assert 78.5 < field < 78.6
    assert 31.4 < circumference < 31.5



if __name__ == '__main__'

