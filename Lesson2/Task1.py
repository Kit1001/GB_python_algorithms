while True:
    operator = input("Введите знак операции (+, -, /, * или 0 для выхода): ")

    if operator == '0':  # завершение программы при вводе 0
        break
    elif operator in {'+', '-', '/', '*'}:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))
        if operator == '+':
            print(f'Сумма чисел равна {num_1 + num_2}')
        elif operator == '-':
            print(f'Разность чисел равна {num_1 - num_2}')
        elif operator == '/':
            if num_2 == 0:
                print('Ошибка, нельзя делить на ноль')  # Собщение об ошибке, если пользователь делит на 0
                continue
            else:
                print(f'Частное чисел равно {num_1 / num_2}')
        elif operator == '*':
            print(f'Произведение чисел равно {num_1 * num_2}')
    else:
        print('Ошибка, неверный знак!')  # Сообщение об ошибке в случае, если пользователь ввел неверный знак
        continue
