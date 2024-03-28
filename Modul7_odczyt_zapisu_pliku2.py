#druga skrócona wersja kodu

passed = []
with open('students.txt', encoding ='utf8') as input_file, open('output.txt', encoding='utf8', mode= 'w') as output_file:
    for line in input_file:
        first_name, last_name, note = line.strip().split(';')
        if note == '2':
            output_file.write(f'{first_name};{last_name};{note}\n')