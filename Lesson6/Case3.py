import psutil

nums = list(range(500000))
temp_nums = list(range(500002))
for i in nums:
    if 0 < i < 500002:
        temp_nums[i] = 0

for i in temp_nums:
    if i > 0:
        num = i
        break

print(psutil.Process().memory_info().rss / (1024*1024))  # 36.5
