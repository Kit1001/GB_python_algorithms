import random


def merge_sort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = int(len(l) / 2)
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


random.seed(42)

some_list = [random.uniform(-0, 49) for _ in range(100)]
print(some_list)  # [31.331913124436305, 1.22552700591068, 13.476436600086844, 10.937326169292314, 36.087089494036604...
some_list_sorted = merge_sort(some_list)
print(some_list_sorted)  # [0.3184392242249898, 1.22552700591068, 1.3002625145093176, 1.4600637524654467...
