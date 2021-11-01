span = range(2, 100)
aliquots = range(2, 10)
result = []

for k in aliquots:
    counter = 0
    for i in span:
        if i % k == 0:
            counter += 1
    result.append((k, counter))

print('В указанном промежутке:')
for number, counter in result:
    print(f'{number} кратно {counter} чисел')
