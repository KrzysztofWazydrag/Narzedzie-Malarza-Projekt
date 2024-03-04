# Napisz funkcję, która wczyta tekst i wypisuje wszystkie wyrazy,
# które zaczynają się na spółgłoskę i kończą na samogłoskę.

def filter_words(text: str) -> set:
    result = set()
    for word in text.split(' '):
        if word[0].lower() not in 'aeiouyąę' and word[-1].lower() in 'aeiouyąę':
            result.add(word)

    return result


def test_filter_words():
    assert filter_words('Ala ma kota') == {'ma', 'kota'}
    assert filter_words('Ala MA KOTA') == {'MA', 'KOTA'}
    assert filter_words('Ala Ma kotA') == {'Ma', 'kotA'}
    assert filter_words('tygrys') == set()
