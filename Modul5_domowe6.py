#Przygotuj funkcje, która odbierze dwa punkty w postaci tupli (x,y). Wynikiem powinna
#być długość odcinka utworzonego w wyniku połączenia tych dwóch punktów.
#wzór : sqrt|AB| = (x2 i x1)**2 + (y2 - y1)**2
#pierwiastek to sqrt   (from math import sqrt)
from math import sqrt


def calculate_segment_lenght(start: tuple, end:tuple) ->float:
    x1, y1 = start
    x2, y2 = end

    return sqrt((x2-x1)**2 + (y2 - y1)**2)

length = calculate_segment_lenght((0,0), (0,4))

print(length)