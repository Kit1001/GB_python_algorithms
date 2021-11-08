import psutil

nums = list(range(500000))
temp_nums = set()
for i in nums:
    if i > 0:
        temp_nums.add(i)

for i in range(1, 2 ** 31):
    if i not in temp_nums:
        num = i
        break

print(psutil.Process().memory_info().rss / (1024*1024))  # 48.83
