def get_vowels(word):
    vowels_in_word = set()
    vowels = 'aeiouyóąę'
    for vowel in vowels:
        if vowel in word or vowel.upper() in word:
            vowels_in_word.add(vowel)

    return vowels_in_word

print(get_vowels('anonymous'))