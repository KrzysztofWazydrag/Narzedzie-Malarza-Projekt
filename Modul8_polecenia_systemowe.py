import subprocess

question = input('Podaj nazwę domeny którą chcesz sprawdzić: ')

process = subprocess.run(['ping', '-n', '1', question], shell=True, capture_output=True)
if 'could not find' in process.stdout.decode('utf8'):
    print(f'Adres {question} jest niedostępny.')
else:
    print(f'Adres {question} jest dostępny')