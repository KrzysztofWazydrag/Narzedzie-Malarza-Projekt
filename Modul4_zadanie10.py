#Napisz program, który będzie usuwał z tekstu wszystkie słowa zaczynające się na wybraną literę.


zdanie = 'Python to fajny jezyk programowania dlatego ucze sie go prawie codziennie'
wykluczona_litera = 'p'

nowe_zdanie = []
for slowo in zdanie.split(' '):
    if not slowo.lower().startswith(wykluczona_litera):
        nowe_zdanie.append(slowo)

print(' '.join(nowe_zdanie))

