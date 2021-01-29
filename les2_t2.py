
num1 = input('Введите число: ')
even = 0
odd = 0
for f in num1:
    i = int(f)
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В число {num1} входят {even} четных цифры и {odd} нечетных')