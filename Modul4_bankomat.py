from time import sleep

print("Witamy w zajebistym bankomacie!!!")
sleep(2)
print("Proszę włożyć kartę")
sleep(3)
print('Proszę czekać')
sleep(3)
print('---' * 4)
sleep(2)
print('---' * 3)
sleep(2)
print('---' * 2)
sleep(2)
print('---' * 1)

current_balance = 1000
new_balance = 0
while True:
    decision = input(
        'Wybierz operację do wykonania:\n'
        '1- wpłata środków,\n'
        '2- wypłata środków,\n'
        '3- stan konta,\n'
        '4- wyjście\n  '
    )
    decision = int(decision)

    if decision == 1:
        pay = int(input('Jaką kwotę chcesz wpłacić? '))
        new_balance = current_balance + pay
        sleep(1)
        print(f"Twój nowy stan konta wynosi:{new_balance} ")
        current_balance += pay
    elif decision == 2:
        pay2 = int(input('Jaką kwotę chcesz wypłacić? '))
        new_balance = current_balance - pay2
        sleep(1)
        print(f"Twój nowy stan konta wynosi:{new_balance} ")
        current_balance -= pay2
    elif decision == 3:
        print('Obecny stan konta wynosi', current_balance)
    else:
        print("Dziękujemy")
        quit()