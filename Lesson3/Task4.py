from random import randint

some_list = [randint(0, 9) for i in range(10)]

# numbers_dict - это словарь, где ключами будут числа из списка, а значения - как часто они встречаются
numbers_dict = {}
for number in some_list:
    if number in numbers_dict:
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

# среди пар ключ-значение словаря, выбираем пару с макс.значением
max_enc_number = max(numbers_dict.items(), key=lambda x: x[1])

# в получившейся паре - первый элемент это число из списка some_list, а второй - кол-во его вхождений в список
print(f'В списке {some_list}\nЧисло {max_enc_number[0]} встречается чаще всего: {max_enc_number[1]} раз(а)')
