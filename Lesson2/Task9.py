repeats = int(input('Введите кол-во вводимых чисел: '))
max_sum = 0
max_number = 0
for i in range(repeats):
    number = input(f'Введите число #{i + 1}: ')
    sum_of_digits = 0

    for digit in number:
        sum_of_digits += int(digit)  # Сумма цифр в числе

    if sum_of_digits > max_sum:
        max_sum = sum_of_digits  # Макс. сумма цифр в числе
        max_number = number

print(f'Число с максимальной суммой цифр: {max_number}\nСумма цифр: {max_sum}')
