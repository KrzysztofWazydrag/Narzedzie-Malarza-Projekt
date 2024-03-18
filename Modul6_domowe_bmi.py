#Przygotuj funkcję, która będzie liczyła BMI na podstawie argumentów:
#wzrost oraz waga. (BMI = masa(kg) / wzrost (m) ** 2
# Druga funkcja powinna na podstawie wartości liczbowej BMI
# opisywać wynik za pomocą tekstu:
# mniej niż 16 - wygłodzenie
# 16- 16,99 - wychudzenie
# 17 - 18,99 - niedowaga
# 18,5 - 24,99 - wartość prawidłowa
# 25 - 25,99 - nadwaga
# 30 - 34,99 - otyłość I stopnia
# 35 - 39,99 - otyłość II stopnia
# powyżej 40 - skrajna otyłość

def calculate_bmi(weight:float, height: float):
    return weight / height ** 2

def bmi_to_text(bmi_score: float) ->str:
    if bmi_score < 16:
        return 'wygłodzenie'
    elif 16 <= bmi_score <= 16.99:
        return 'wychudzenie'
    elif 17 <= bmi_score <= 18.49:
        return 'niedowaga'
    elif 18.5 <= bmi_score <= 24.99:
        return 'wartość prawidłowa'
    elif 25 <= bmi_score <= 29.99:
        return 'nadwaga'
    elif 30 <= bmi_score <= 34.99:
        return 'otyłość I stopnia'
    elif 35 <= bmi_score <= 39.99:
        return 'otyłość II stopnia'
    else:
        return 'skrajna otyłość'

def test_correct_bmi():
    bmi = calculate_bmi((75, 1.82))
    assert 22 < bmi < 23
    assert  bmi_to_text(bmi) == 'wartość prawidłowa'

def test_bmi_to_text():
    assert bmi_to_text(16.5) == 'wychudzenie'
    assert bmi_to_text(12) == 'wygłodzenie'
    assert bmi_to_text(18) == 'niedowaga'
    assert bmi_to_text(35) == 'otyłość II stopnia'

def __name__ = '__main__':
    weight = float(input('Podaj wagę w kg: '))
    height = float(input('Podaj wzrost w m: '))

    bmi = calculate_bmi(weight,height)
    bmi_text = bmi_to_text(bmi)




