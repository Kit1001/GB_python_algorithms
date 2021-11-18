# Скрипт берет случайное число из списка и формирует два списка, в одном все числа больше, в другом меньше случайного.
# Далее сравнивается размер двух списков и процедура повторяется для большего списка
# пока не получится два одинаковых по размеру списка, с медианой в середине.
import random
import time


def find_median(list_, n=0):
    random_index = random.randint(0, len(list_) - 1)
    list_a, list_b, list_c = [], [], []
    num = list_[random_index]
    for x in list_:
        if x < num:
            list_a.append(x)
        elif x > num:
            list_b.append(x)
        else:
            list_c.append(x)
    # в случае если случайное число встречается несколько раз, необходимо исключить его только 1 раз
    # поэтому возвращаем его в списки. Нащупал это решение на практике, не до конца понимаю, почему без этого
    # алгоритм ломается, если числа в списке не уникальные
    if len(list_c) > 1:
        while len(list_c) != 1:
            append = list_a if len(list_c) % 2 == 0 else list_b
            append.append(list_c.pop())
    if len(list_a) + n == len(list_b):
        return list_[random_index]
    elif len(list_a) + n > len(list_b):
        n -= len(list_b) + 1
        return find_median(list_a, n)
    elif len(list_b) > len(list_a) + n:
        n += len(list_a) + 1
        return find_median(list_b, n)


random.seed(42)
some_list = [random.randint(-100, 100) for _ in range(random.randint(5, 50000) * 2 + 1)]
start = time.time()
# ищем медиану через функцию, получается 1, время выполнения ~ 0.023
print('median result', find_median(some_list), round((time.time() - start), 4))
start = time.time()
# проверяем результат с помощью сортировки, результат 1, время выполнения 0.008. Мой алгоритм медленнее почти в 3 раза
print('sorted result', sorted(some_list)[len(some_list) // 2], round((time.time() - start), 4))
