# Przygotuj funkcje, ktora bedzie potrafiła przefiltrować liczby parzyste z listy przekazanej w argumencie.

def numbers_filter(list1:list) ->list:
    evens = []
    for numb in list1:
        if numb % 2 == 0:
            evens.append(numb)

    return evens

print(numbers_filter([1,2,3,4,5,6,7,8,9]))

# przygotuj funkcję, która przefiltruje tylko słowa których długość jest większa od 4 i mniejsza od 8

def check_words_length(args:list) ->list:
    four_to_eight = []
    for word in args:
        if 4<len(word)<8:
            four_to_eight.append(word)

    return four_to_eight

print(check_words_length(['cat', 'lama','tiger','elephant','giraffe']))

# Przygotuj funkcję, która zliczy ilość znaków w tekście zawierających się wewnątrz nawiasów okrągłych.
# Nawiasy mogą występować w tekście wielokrotnie, nigdy nie będą się w sobie zawierać.

def count_char_between(text, char_start:str='(', char_end:str=')'):
    should_i_count_char = False
    counter = 0

    for char in text:
        if char == char_end:
            should_i_count_char = False

        if should_i_count_char:
            counter += 1

        if char == char_start:
            should_i_count_char = True

    return counter


print(count_char_between('Ala ma (kota)'))
print(count_char_between('(Ala) ma (kota)'))
