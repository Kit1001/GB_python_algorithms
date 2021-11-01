from random import randint
from copy import copy

some_list = [randint(0, 9) for i in range(10)]
some_list_orig = copy(some_list)

#  Узнаем мин. и макс. значения в списке some_list
#  Составляем другой список modifications, куда записываем кортежи из индексов мин. или макс. элемента и
#  противоположного значения, чтобы потом внести эти изменения в список some_list

min_value = min(some_list)
max_value = max(some_list)

modifications = []  # список кортежей, которые содержат индекс и значение для записи изменений в список

for idx, number in enumerate(some_list):
    if number == min_value:
        modifications.append((idx, max_value))
    elif number == max_value:
        modifications.append((idx, min_value))


for idx, val in modifications:  # здесь производится запись необходимых изменений по списку modifications
    some_list[idx] = val

print('Оригинальный список:\n', some_list_orig)
print('Измененный список:\n', some_list)
print(f'Меняли местами {max_value} и {min_value}')
