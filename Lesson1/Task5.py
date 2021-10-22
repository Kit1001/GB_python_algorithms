# проверка, что пользователь ввел один символ
try:
    symbol_1 = ord(input('Введите первую букву: ').lower())
    symbol_2 = ord(input('Введите вторую букву: ').lower())
except TypeError:
    raise TypeError('Нужно ввести только одну букву')

# проверка, что пользователь ввел символы из латинского алфавита
if 96 < symbol_1 < 123 and 96 < symbol_2 < 123:
    print(f'"{chr(symbol_1)}" это {symbol_1 - 96} буква алфавита')
    print(f'"{chr(symbol_2)}" это {symbol_2 - 96} буква алфавита')

    letters_between = abs(symbol_2 - symbol_1) - 1
    letters_between = 'нет букв' if letters_between < 1 else f'{letters_between} букв'
    print(f'Между ними {letters_between}')
else:
    raise TypeError('Нужно ввести буквы из латинского алфавита')
