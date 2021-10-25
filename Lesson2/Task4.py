n = int(input('Введите количество элементов: '))
counter = 0
number = 1
result = 0

while counter < n:
    result += number
    number = number / (-2)  # Последовательность начинается с 1, каждое след. число делится на -2
    counter += 1
print('Сумма равна:', result)
