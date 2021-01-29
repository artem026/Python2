
range1 = input('Введите последовательность чисел - ')
num1 = input('Введите цифру из последовательности - ')
count = 0

for i in range1:
    if i == num1:
        count += 1

print(f'Цифра {num1} встречается {count} раз в последовательности {range1}')
