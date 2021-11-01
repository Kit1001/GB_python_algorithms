"""
Для сравнения разных алгоритмов выбрал задачу №4 из второго урока.
Сравниваю решения через цикл for..in, цикл while и рекурсию
Получилось, что в среднем for..in справляется в 1.5 раза быстрее, чем while, а while в 1.6 раза быстрее рекурсии
"""


from time import time
import gc


def count_cycle_for(n):
    result = 0
    number = 1
    for _ in range(n):
        result += number
        number = number / (-2)
    return result


def count_cycle_while(n):
    result = 0
    number = 1
    while n > 0:
        result += number
        number = number / (-2)
        n -= 1
    return result


def count_recursion(m, n=1):
    if m == 1:
        return n
    else:
        return n + count_recursion(m - 1, n / (-2))


def time_func(func, arg, repeats=10**4):
    # функция замеряет время выполнения переданной в нее функции func. Результат - среднее для 10 тыс.повторений
    result = []
    for _ in range(repeats):
        gc.disable()
        start = time()
        func(arg)
        stop = time()
        gc.enable()
        time_taken = stop - start
        result.append(time_taken)
    return sum(result) / len(result)


reps = 997
time_cycle_for = time_func(count_cycle_for, reps)
time_cycle_while = time_func(count_cycle_while, reps)
time_recursion = time_func(count_recursion, reps)

print(f'Цикл for in быстрее цикла while в {time_cycle_while / time_cycle_for:.2f} раз(а)')
print(f'Цикл while быстрее рекурсии в {time_recursion / time_cycle_while:.2f} раз(а)')
