container = []

for question in range(10):
    while True:
        try:
            user_input = int(input(f'Podaj {question +1} liczbę dodatnią: '))
            if user_input > 0:
                container.append(user_input)
                break
            else:
                print('Podano nieprawidłową wartość. Podaj liczbę dodatnią')
        except ValueError:
            pass

print(max(container))
print(min(container))

