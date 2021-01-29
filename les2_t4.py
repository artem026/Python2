
n = int(input('Введите количество элементов: '))
i = 0
element = 1
sum1 = 0
while i < n:
    sum1 += element
    element *= -0.5
    i += 1

print(f'Сумма элементов равна {sum1}')
