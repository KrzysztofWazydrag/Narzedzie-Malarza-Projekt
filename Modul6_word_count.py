#Przygotuj funkcję, która zlicza ilość wystąpień jednego słowa w tekście np.
#count_word('Python i Python', 'Python') da wynik 2

def word_count(haystack:str, needle: str) -> int:
    counter = 0
    for word in haystack.split(' '):
        if word.lower() == needle.lower():
            counter += 1

    return counter

def test_word_count():
    assert word_count('Python i Python', 'Python') == 2
    assert word_count('python i python', 'Python') == 2
    assert word_count('Python i Python', 'Java') == 0
    assert word_count('Hej hej hej sokoły, omijajcie ...', 'hej') == 3


