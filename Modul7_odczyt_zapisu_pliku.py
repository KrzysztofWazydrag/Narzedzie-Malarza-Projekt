#strip() usunęło niepotrzebne spacje
#encoding = 'utf8' przywróciło polskie znaki
#pierwsza wersja kodu - długa
passed = []

with open('students.txt', encoding ='utf8') as file:
    for line in file:
        first_name, last_name, note = line.strip().split(';')
        if note == '2':
            passed.append({'first_name': first_name, 'last_name': last_name, 'note': note})

with open('output.txt', encoding='utf8', mode= 'w') as file:
    for student in passed:
        file.write(f'{student.get("first_name")};{student.get("last_name")};{student.get("note")}\n')