from random import randint

some_list = [randint(-99, 99) for i in range(10)]

# фильтруем из списка все числа меньше 0, берем элемент с макс. значением
max_neg_number = max([i for i in some_list if i < 0])
print(f'В списке\n{sorted(some_list)}')
print(f'максимальное отрицательное число: {max_neg_number}')
