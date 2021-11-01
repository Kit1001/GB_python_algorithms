import collections

enterprise = collections.namedtuple('Enterprise', ['name', 'income_1', 'income_2', 'income_3', 'income_4'])
e_list = []

n = int(input('Введите количество предприятий: '))
for i in range(n):
    name = input(f"Введите название предприятия №{i+1}: ")
    income_1 = float(input(f'Введите прибыль {name} за 1 квартал: '))
    income_2 = float(input(f'Введите прибыль {name} за 2 квартал: '))
    income_3 = float(input(f'Введите прибыль {name} за 3 квартал: '))
    income_4 = float(input(f'Введите прибыль {name} за 4 квартал: '))
    e_list.append(enterprise(name, income_1, income_2, income_3, income_4))

# Можно раскоментить, чтобы не вводить данные руками
# e_list = []
# e_list.append(enterprise('Abc', 50.5, 33.3, 67.3, 97.6))
# e_list.append(enterprise('Cde', 123.32, 170.75, 120.64, 125))
# e_list.append(enterprise('Fgh', 65.67, 50.4, 34.5, 150.54))
# e_list.append(enterprise('Ijk', 75, 115, 99, 95))

avg = sum([sum(i[1:5]) for i in e_list]) / len(e_list)
avg_above = [i[0] for i in e_list if sum(i[1:5]) >= avg]
avg_below = [i[0] for i in e_list if sum(i[1:5]) < avg]

print(f'Предприятия, чья годовая прибыль выше средней: {avg_above}')
print(f'Предприятия, чья годовая прибыль ниже средней: {avg_below}')
print(e_list[0])
