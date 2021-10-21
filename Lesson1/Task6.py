# проверка, что пользователь ввел число
try:
    letter = int(input('Введите номер буквы в алфавите: '))
except ValueError:
    raise ValueError('Нужно ввести число')

# проверка, что пользователь ввел число от 1 до 26
if 0 < letter < 27:
    print(f'{letter} буква латинского алфавита это: {chr(letter + 96).upper()}')
else:
    raise ValueError('Число должно быть от 1 до 26')
