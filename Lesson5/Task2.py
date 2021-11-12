number_1 = input('Введите число 1: ').upper()
number_2 = input('Введите число 2: ').upper()

# Сохраняем числа в виде списка
number_1, number_2 = list(number_1), list(number_2)
print("Число 1:", number_1)
print("Число 2:", number_2)

# Конвертируем в десятичную систему счисления
num_1_conv = int(''.join(number_1), 16)
num_2_conv = int(''.join(number_2), 16)

total_add = hex(num_1_conv + num_2_conv)
total_add = list(total_add[2:].upper())
print('Сумма:', total_add)

total_multiply = hex(num_1_conv * num_2_conv)
total_multiply = list(total_multiply[2:].upper())
print("Произведение:", total_multiply)
