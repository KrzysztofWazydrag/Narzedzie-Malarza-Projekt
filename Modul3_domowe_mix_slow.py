from random import choice, shuffle

words = ['koziołek', 'baranek', 'bażant', 'stokrotka','wesołek', 'grafitti','palermo']
selected_word = choice(words)
letters = list(selected_word)
shuffle(letters)
print('Słowo do odgadnięcia to: ', ''.join(letters))

for a in range(3):
    answer = input('Czy wiesz jakie to słowo: ')

    if answer == selected_word:
        print(f"Brawo, odgadłeś za {a + 1} razem")
        break
    else:
        print("Spróbuj jeszcze raz")