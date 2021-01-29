while True:
    operation = input('Введите математическую перацию ( +, -, *, /, 0): ')
    if oper == '0':
        break
    if operation in {'+', '-', '*', '/', }:
        num1 = int(input('number 1 ='))
        num2 = int(input('number 2 ='))

        if operation == '+':
            print(f'{num1} {operation} {num2} = {num1 + num2}')
        elif operation == '-':
            print(f'{num1} {operation} {num2} = {num1 - num2}')
        elif operation == '*':
            print(f'{num1} {operation} {num2} = {num1 * num2}')
        elif operation == '/':
            print(f'{num1} {operation} {num2} = {num1 / num2}')
        else:
            print('Ошибка. Деление на ноль')
    else:
        print('Ошибка')
