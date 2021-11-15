import random


def bubble_sort(li):
    for n in range(1, len(li) - 1):
        for i in range(len(li) - n):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]


random.seed(42)

some_list = [random.randint(-100, 99) for _ in range(1000)]
print(some_list)   # [63, -72, -94, 89, -30, -38, -43, -65, 88, -74, 73, 89, 39, -78, 51, 8, -92, -93, -77, -45...
bubble_sort(some_list)
print(some_list)  # [-100, -100, -100, -100, -100, -100, -99, -99, -99, -99, -98, -98, -98, -98, -98, -97...
