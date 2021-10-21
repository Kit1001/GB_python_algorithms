# проверка, что пользователь ввел число
try:
    year = int(input('Введите год: '))
except ValueError:
    raise ValueError('Нужно ввести число')

# проверка, что число больше 0
if year < 0:
    raise ValueError('Год должен быть положительным числом')

if year < 1582:
    if year % 4 == 0 and year > 7:
        print('Високосный')
    else:
        print('Невисокосный')
else:
    if year % 400 == 0:
        print('Високосный')
    elif year % 100 == 0 or year % 4 != 0:
        print('Невисокосный')
    else:
        print('Високосный')
