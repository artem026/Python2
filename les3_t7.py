import random

arr = [random.randint(0, 99) for _ in range(20)]
print(f'Исходный массив: {arr}')

min_ind1 = 0
min_ind2 = 1

for i in arr:
    if arr[min_ind1] > i:
        min_ind2 = min_ind1
        min_index_1 = arr.index(i)
    elif arr[min_ind2] > i:
        min_ind2 = arr.index(i)

print(f'Два наименьших элемента: {arr[min_ind1]} и {arr[min_ind2]}')
