# Przygotuj program który bedzie szyfrował i odszyfrowywał wyrażenia korzystajac
# z szyfru Cezara. Podpowiedz: mogą ci sie przydac funkcje ord() oraz chr()

SECRET = 3
text = input('Podaj mi tekst do przetworzenia: ')
action = input('1. Odszyfruj, 2. Zaszyfruj: ')
text = text.upper()

encrypted_text = ''
for char in text:
    if char.isalpha():
        if action == '1':
            char = chr((ord(char) - SECRET - ord('A')) % 26 + ord('A'))
        elif action == '2':
            char = chr((ord(char) + SECRET - ord('A')) % 26 + ord('A'))

    encrypted_text += char

print(encrypted_text)


"""wytlumaczenie ord() i chr() poniżej"""
# ord(): Funkcja ord() przyjmuje pojedynczy znak tekstowy jako argument i
# zwraca jego kod Unicode (liczbę całkowitą reprezentującą ten znak). Na przykład:
char = 'A'
unicode_code = ord(char)
print(f"Kod Unicode dla '{char}' to: {unicode_code}")
# W tym przypadku, unicode_code będzie równa 65,
# ponieważ 65 to kod Unicode dla wielkiej litery 'A'.

#chr(): Funkcja chr() działa w odwrotny sposób.
# Przyjmuje liczbę całkowitą (kod Unicode) i zwraca odpowiadający jej znak. Przykład:
unicode_code = 65
character = chr(unicode_code)
print(f"Znak o kodzie Unicode {unicode_code} to: {character}")
#W tym przypadku, character będzie równa 'A', p
# onieważ 65 to kod Unicode dla wielkiej litery 'A'.
# Te dwie funkcje są używane do przekształcania znaków między postacią tekstową
# a ich reprezentacją numeryczną w systemie Unicode.