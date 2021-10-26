some_list = [8, 3, 15, 6, 4, 2]

result = []
for i, v in enumerate(some_list):
    if v % 2 == 0:
        result.append(i)
print(result)
