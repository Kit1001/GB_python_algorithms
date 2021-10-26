counter = 0

for i in range(32, 128):
    print(f'{i: >03} - {chr(i)}', end='    ')
    counter += 1
    if counter % 10 == 0:  # Новая строка через каждые 10 элементов
        print('')
