import random

number = random.randint(1,100)


counter = 0
while True:
    user_guess = int(input('Guess number: '))
    counter += 1
    if number == user_guess:
        print(f'Brawo, zgadłeś/zgadłaś numer po {counter} próbach')
        break
    elif number > user_guess:
        print('Za mała')
    else:
        print('Za duża')