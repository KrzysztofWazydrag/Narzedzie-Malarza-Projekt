from random import sample
from math import ceil
from string import ascii_lowercase, ascii_uppercase

def generate_password(length, upper_letters=False, lower_letters=False, numbers=False, specials=False):
    special_chars= '!@#$%^&*()'
    password = ''
    characters = [upper_letters, lower_letters, numbers, specials]

    if upper_letters:
        password += ''.join(sample(ascii_uppercase, ceil(length / sum(characters))))

    if lower_letters:
        password += ''.join(sample(ascii_lowercase, ceil(length / sum(characters))))

    if specials:
        password += ''.join(sample(special_chars, ceil(length / sum(characters))))

    if numbers:
        password += ''.join(sample('123456789', ceil(length / sum(characters))))

    print(password)



generate_password(10, upper_letters=True, lower_letters=True, numbers=True, specials=True)