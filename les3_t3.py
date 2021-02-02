import random

arr = [random.randint(0, 20) for _ in range(20)]
print(f'Исходный массив: {arr}')

max_elem = arr[0]
min_elem = arr[0]

for i in arr:
    if i > max_elem:
        max_elem = i
    elif i < min_elem:
        min_elem = i
min_index = arr.index(min_elem)
max_index = arr.index(max_elem)
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(f'Массив после перестановки местами элементов {min_index} и {max_index}: {arr}')
