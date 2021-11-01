from time import time
import gc


def simple_number(n):
    counter = 0
    number = 1
    while counter < n:
        number += 1
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            counter += 1
    return number


def sieves(k):
    b = []
    n = 10
    while len(b) < k:
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

        b = []
        for i in a:
            if a[i] != 0:
                b.append(a[i])
        n *= 10
    return b[k - 1]


def time_func(func, arg, repeats=10**4):
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
