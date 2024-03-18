# Przygotuj program, który wyświetli datę Twoich następnych urodzin oraz
# odpowie na pytanie ile musisz na nie czekać dni.

#Jeśli dzień Twoich urodzin w danym roku już minął powinna pokazać się data w roku następnym.

from datetime import date

today = date.today()
next_birthday = date(today.year, 7, 16)

if today > next_birthday:
    next_birthday = date(today.year + 1, 7, 16)

print(f'Twoje urodziny odbędą się', next_birthday.strftime('%a, %d.%m.%Y'))