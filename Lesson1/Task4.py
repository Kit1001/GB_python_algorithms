import random

# проверка, что пользователь ввел число
try:
    print("Случайное целое число:")
    integer_min = int(input('от '))
    integer_max = int(input('до '))
except ValueError:
    msg = 'Нужно ввести число'
    raise ValueError(msg)

# если первое число больше второго, меняем их местами для корректной работы randint()
if integer_min > integer_max:
    integer_min, integer_max = integer_max, integer_min
print(random.randint(integer_min, integer_max), '\n')

# проверка, что пользователь ввел число
try:
    print("Случайное вещественное число:")
    float_min = float(input('от '))
    float_max = float(input('до '))
except ValueError:
    msg = 'Нужно ввести число'
    raise ValueError(msg)

print(random.uniform(float_min, float_max), '\n')

# проверка, что пользователь ввел один символ, регистр игнорируем
try:
    print("Случайный символ(из латинского алфавита от a до z):")
    sym_min = ord(input('от ').lower())
    sym_max = ord(input('до ').lower())
except TypeError:
    msg = 'Нужно ввести только один символ'
    raise TypeError(msg)

# проверка, что символ относится к диапазону латинского алфавита
if 96 < sym_min < 123 and 96 < sym_max < 123:
    # если первое число больше второго, меняем их местами для корректной работы randint()
    if sym_min > sym_max:
        sym_min, sym_max = sym_max, sym_min
    print(chr(random.randint(sym_min, sym_max)))
else:
    raise TypeError('Допустимы только символы латинского алфавита')
