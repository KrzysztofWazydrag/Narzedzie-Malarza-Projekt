translation = {'dog':'pies', 'cat':'kot', 'mouse':'mysz','ball':'piłka','eagle':'orzeł'}

language = input('w jakim języku chcesz wyswietlic tlumaczenie: ')
translated_word = None

if language not in ['Ang', 'Pol']:
    print('Nie wiem co chcesz zrobić')
    quit()

word = input('podaj słowo do tlumaczenia: ')
translated_word = None
for english_word, polish_word in translation.items():
    if language == 'Ang' and english_word == word:
        translated_word = polish_word
        break
    elif language == 'Pol' and polish_word == word:
        translated_word = english_word
        break

if translated_word is not None:
    print(f'Tłumaczenie to {translated_word}')
else:
    print('Nie znam tego słowa')

