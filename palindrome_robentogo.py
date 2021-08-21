input = input('Silahkan Input: ')
check = input == input[::-1]

if check:
    print('ini palindrome')
else:
    print('bukan palindrom')