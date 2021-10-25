repeats = int(input('Введите кол-во вводимых чисел: '))
ref_digit = int(input('Введите цифру, чье кол-во необходимо посчитать: '))
count = 0

for i in range(repeats):
    number = input(f'Введите число #{i+1}: ')
    for digit in number:
        if ref_digit == int(digit):
            count += 1

print(f'Искомая цифра встречается в введенных числах {count} раз')
