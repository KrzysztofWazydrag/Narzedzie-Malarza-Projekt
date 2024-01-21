#utworz talie kart

from random import choices, shuffle

values = list(range(2,11)) + ['J', 'Q', 'K', 'A']
colors = [chr(9824), chr(9827), chr(9829), chr(9830)]
all_cards = []

for color in colors:
    for value in values:
        all_cards.append(f'{value}{color}')

print(choices(all_cards, k=2))
shuffle(all_cards)
print(all_cards[:2])
print(all_cards.pop(), all_cards.pop())