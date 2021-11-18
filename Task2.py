from collections import Counter
from time import sleep


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def build_code_table(node):
    code_table = {}
    node_list = [(node, '')]
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

    return code_table


string = 'Мама мыла раму!'
c = Counter(string)
# print(c.items())
c = [(k, v) for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True)]
print(c)

while len(c) > 1:
    first = c.pop()
    second = c.pop()
    tmp = Node(first[0], second[0])
    tmp_sum = first[1] + second[1]
    c.append((tmp, tmp_sum))
    c.sort(key=lambda x: x[1], reverse=True)
    # print(c)
else:
    c = c[0][0]


# print(c.left.right.right)
print(build_code_table(c))
