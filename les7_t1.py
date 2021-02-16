import random

num_min = -100
num_max = 99
array = [random.randint(num_min, num_max) for _ in range(10)]

print(array)


def sort_1(arr):
    for n in range(1, len(arr)):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


sort_1(array)
print(array)
