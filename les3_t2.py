import random

arr = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {arr}')
index_even = []

for n in arr:
    if n % 2 == 0:
        index_even.append(arr.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}')
