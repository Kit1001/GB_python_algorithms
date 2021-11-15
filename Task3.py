# Скрипт берет случайное число из списка и формирует два списка, в одном все числа больше, в другом меньше случайного.
# Далее сравнивается размер двух списков и процедура повторяется для большего списка
# пока не получится два одинаковых по размеру списка, с медианой в середине.
import random


def find_median(list_, n=0):
    random_index = random.randint(0, len(list_) - 1)
    list_a = [x for x in list_ if x <= list_[random_index]]
    list_b = [x for x in list_ if x > list_[random_index]]
    if len(list_a) + n == len(list_b):
        return list_[random_index]
    elif len(list_a) + n > len(list_b):
        n -= len(list_b) + 1
        return find_median(list_a, n)
    elif len(list_b) > len(list_a) + n:
        n += len(list_a) + 1
        return find_median(list_b, n)


random.seed(42)
some_list = [random.randint(-100, 100) for _ in range(random.randint(5, 5000) * 2 + 1)]
print('median result', find_median(some_list))  # получается 3
print('sorted result', sorted(some_list)[len(some_list) // 2])  # проверяем результат с помощью сортировки
