from collections import Counter
from time import sleep


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def archive(string):
    container = Counter(string)
    # превращаем Counter в список кортежей, где первый элемент - подстрока, а второй - кол-во вхождений
    container = [(k0, v0) for k0, v0 in sorted(container.items(), key=lambda x: x[1], reverse=True)]

    # Берем 2 последних элемента списка container и соединяем их в ноду, складываем кол-во их вхождений
    # и включаем ноду обратно в container, сортируем по кол-ву вхождений, пока не останется одна нода - вершина дерева
    while len(container) > 1:
        first = container.pop()
        second = container.pop()
        tmp = Node(first[0], second[0])
        tmp_sum = first[1] + second[1]
        container.append((tmp, tmp_sum))
        container.sort(key=lambda x: x[1], reverse=True)
    else:
        container = container[0][0]  # из контейнера нам теперь нужна только ссылка на начало дерева

    # Проходим по получившемуся дереву, составляя таблицу кодирования
    code_table = {}
    node_list = [(container, '')]
    tmp_list = []

    while len(node_list) > 0:
        for node, code in node_list:
            if type(node.left) is str:
                code_table[node.left] = f'{code}0'
            if type(node.right) is str:
                code_table[node.right] = f'{code}1'

            if type(node.left) is Node:
                tmp_list.append((node.left, f'{code}0'))
            if type(node.right) is Node:
                tmp_list.append((node.right, f'{code}1'))

        node_list = tmp_list
        tmp_list = []

    # Кодируем исходную строку с помощью таблицы
    coded_string = []
    for i in string:
        coded_string.append(code_table[i])

    return coded_string, code_table  # Возвращаем закодированную строку и таблицу кодирования


string_ = 'Мама мыла раму!'
archived_string = archive(string_)
print(*archived_string[0])
for k, v in archived_string[1].items():
    print(k, '-', v)
