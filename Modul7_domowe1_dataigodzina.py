# Napisz program, który wyświetli bieżącą datę i godzinę w formacie "dd/mm/rrrr, godzina:minuta:sekunda

from datetime import datetime

time_now = datetime.now()
time_now.strftime("%d/%m/%Y %H:%M:%S")
print(time_now)
# current_date = date.today().strftime('%a %d.%m.%Y')
# print(current_date)
# time = time.strftime(current_date)
# print(time)