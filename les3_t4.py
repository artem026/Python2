import random

arr = [random.randint(0, 99) for _ in range(20)]
print(f'Массив: {arr}')

max_index = 0
for i in arr:
    if arr.count(max_index) < arr.count(i):
        max_index = arr.index(i)

print(f'Число {arr[max_index]} встречается: {arr.count(max_index)} раз')
