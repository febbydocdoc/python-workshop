number1 = int(input('masukkan angka pertama: '))
operator = input('pilih operator (+, -, /, *): ')
number2 = int(input('masukkan angka kedua: '))

result = 0
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '/':
    result = number1 / number2
elif operator == '*':
    result = number1 / number2
else:
    print('invalid operatior!')

if result is not None:
    print(f'{number1} {operator} {number2} = {result}')
