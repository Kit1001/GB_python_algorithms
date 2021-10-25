number = input("Введите число: ")
number_len = str(len(number))    # Длина строки нужна, чтобы вывести так же нули в конце числа. Т.е. 10 -> 01, а не 1
number = int(number)
number_rev = 0

while number != 0:
    digit = number % 10
    number //= 10
    number_rev += digit
    number_rev *= 10
else:
    number_rev //= 10

print(f'{" "*15}{number_rev:0{number_len}d}')

"""
Другой вариант решения:
number = input("Введите число: ")
print(f'{" "*15}{number[::-1]}')
"""
