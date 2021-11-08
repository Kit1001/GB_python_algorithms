import psutil

nums = list(range(500000))
extra = 1 << 31
n = len(nums)

for num in nums:
    if num >= extra: num -= 2 * extra
    if num > 0 and num <= n and nums[num - 1] < extra:
        nums[num - 1] += 2 * extra

for i, num in enumerate(nums):
    if num < extra:
        break


print(psutil.Process().memory_info().rss / (1024*1024))  # 40.0
