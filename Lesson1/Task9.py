# проверка, что пользователь ввел число
try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
except ValueError:
    raise ValueError('Нужно ввести число')

if a >= b >= c or a <= b <= c:
    mid = b
elif b >= a >= c or b <= a <= c:
    mid = a
else:
    mid = c

print('Среднее из этих чисел: ', mid)
