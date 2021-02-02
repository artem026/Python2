result = {}
for n in range(2, 10):
    result[n] = []
    for i in range(2, 20):
        if i % n == 0:
            result[n].append(i)
    print(f'Для числа {n} кратны - {len(result[n])} Список чисел: {result[n]}')
