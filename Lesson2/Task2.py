number = int(input("Введите натуральное число: "))
odds = 0
evens = 0
while number != 0:
    digit = number % 10
    number = number // 10

    if digit % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f'Нечетных цифр {odds}\nЧетных цифр {evens}')
