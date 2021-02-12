# Python 3.8.5  [MSC v.1926 32 bit (Intel)] on win32

import random
import sys


arr = [random.randint(0, 99) for _ in range(20)]
print(f'Исходный массив: {arr}')

min_ind1 = 0
min_ind2 = 1

for i in arr:
    if arr[min_ind1] > i:
        min_ind2 = min_ind1
        min_ind1 = arr.index(i)
    elif arr[min_ind2] > i:
        min_ind2 = arr.index(i)

print(f'Два наименьших элемента: {arr[min_ind1]} и {arr[min_ind2]}')  # 9 15

print(f'Размер листа: {sys.getsizeof(arr)}')  # 128
print(f'Размер элемента листа: {sys.getsizeof(arr[0])}')  # 14
print(f'Размер кортежа: {sys.getsizeof(tuple(arr))}')  # 100
print(f'Размер элемента кортежа: {sys.getsizeof(tuple(arr)[0])}')  # 14
sum_1 = 0
for size in arr:
    sum_1 += sys.getsizeof(size)
print(f'Размер всех элементов в листе: {sum_1}')  # 280


# 2 вариант
arr_sort = []
arr_sort.extend(arr)
print(f'Исходный массив 2: {arr_sort}')
arr_sort.sort()

print(f'Два наименьших элемента (второй способ): {arr_sort[0]} и {arr_sort[1]}')  # 9 15

print(f'Размер листа: {sys.getsizeof(arr_sort)}')  # 140
print(f'Размер элемента листа: {sys.getsizeof(arr_sort[0])}')  # 14
print(f'Размер кортежа: {sys.getsizeof(tuple(arr_sort))}')  # 100
print(f'Размер элемента кортежа: { sys.getsizeof(tuple(arr_sort)[0])}')  # 14
sum_2 = 0
for size2 in arr_sort:
    sum_2 += sys.getsizeof(size2)
print(f'Размер всех элементов в листе: {sum_2}')  # 280
