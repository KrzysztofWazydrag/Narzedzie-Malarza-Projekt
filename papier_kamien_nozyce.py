import random

gra = (0, 1, 2)

player = int(input('Papier, nozyce, czy kamien?(0,1,2): '))
computer = random.randrange(0,2)
print(computer)

ilosc_gier = 0
while ilosc_gier < 3:
    if player == 0 and computer == 0:
        print('draw')
    elif player == 1 and computer == 1:
        print('draw')
    elif player == 2 and computer == 2:
        print('draw')
    elif player == 1 > computer == 0 or player == 2 > computer == 1 or player == 0 > computer == 2:
            print('Player wins')
    else:
        print('Computer wins')
    ilosc_gier += 1