from random import randint

number = randint(0, 100)
tries = 0
while tries < 10:
    tries += 1
    answer = int(input(f'Попытка №{tries}. Угадайте число: '))

    if answer == number:
        print('Вы угадали!')
        break
    elif answer > number:
        print('Ваше число больше загаданного')
    else:
        print("Ваше число меньше загаданного")
else:
    print('Попытки кончились, вы не угадали число')
