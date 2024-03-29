with open ('transakcje.txt', encoding='utf8', mode='r') as start_file, open('przychody.txt', encoding='utf8', mode='w') as end_file:
    for line in start_file:
        date, task, cost = line.strip().split(';')
        if int(cost) > 0:
            end_file.write(f'{date},{task},{cost}\n')