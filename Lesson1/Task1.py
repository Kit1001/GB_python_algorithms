# проверка что пользователь ввел число
try:
    number = int(input('Введите трехзначное число\n'))
except ValueError:
    msg = 'Ошибка, нужно ввести число'
    raise ValueError(msg)

# проверка, что число трехзначное
if not (99 < number < 1000):
    msg = 'Ошибка, число должно быть трехзначное'
    raise Exception(msg)

digit_1 = number // 100
number = number % 100
digit_2 = number // 10
number = number % 10
digit_3 = number
print(f'Сумма цифр числа = {digit_3 + digit_2 + digit_1}')
print(f'Произведение цифр числа = {digit_3 * digit_2 * digit_1}')
