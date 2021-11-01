"""
Сравнение времени поиска n-го простого числа простым алгоритмом и решетом Эратосфена.
Простой алгоритм имеет квадратичную сложность, а решето - логарифмическую, поэтому при малом значении n -
разница в скорости выполнения практически отсутствует и вырастает в десятки раз с увеличением n.
"""


from time import time
import gc


def simple_number(n):
    counter = 0
    num = 1
    while counter < n:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            counter += 1
    return num


def sieves(k):
    """
    n - число до которого ищем простое число. Т.к. оно заранее неизвестно,
    каждый цикл n умножается на 10 и поиск повторяется.
    """
    simple_numbers = []
    n = 10
    while len(simple_numbers) < k:
        a = [0] * n
        for i in range(n):
            a[i] = i

        a[1] = 0

        m = 2
        while m < n:
            if a[m] != 0:
                j = m * 2
                while j < n:
                    a[j] = 0
                    j = j + m
            m += 1

        simple_numbers = []
        for i in a:
            if a[i] != 0:
                simple_numbers.append(a[i])
        n *= 10
    return simple_numbers[k - 1]


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


number = 50
my_alg_time = time_func(simple_number, number, repeats=1000)
sieve_time = time_func(sieves, number, repeats=1000)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}\n')

number = 1000
my_alg_time = time_func(simple_number, number, repeats=10)
sieve_time = time_func(sieves, number, repeats=10)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}\n')

number = 5000
my_alg_time = time_func(simple_number, number, repeats=1)
sieve_time = time_func(sieves, number, repeats=1)
print(f'Результат вычисления {number}-го простого числа\n'
      f'Время простого алгоритма: {my_alg_time:.2e}\n'
      f'Время решета: {sieve_time:.2e}\n'
      f'Соотношение: {my_alg_time / sieve_time:.2f}')
