matrix = []
for i in range(4):
    row = input(f'Введите элементы строки {i+1} через пробел: ')
    row = [int(i) for i in row.split(' ')]
    row.append(sum(row))
    matrix.append(row)

print('\nМатрица:')
for row in matrix:
    print(*row)
