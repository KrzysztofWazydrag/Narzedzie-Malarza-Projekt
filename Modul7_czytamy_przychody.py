total_sum = 0

with open('przychody.txt', encoding='utf8', mode='r') as start_file:
    for line in start_file:
        date, task, cost = line.strip().split(',')
        total_sum += int(cost)

print(f'Total amount of tasks is', total_sum)
