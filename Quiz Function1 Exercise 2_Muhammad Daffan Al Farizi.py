def check_upper_lower(str):
    upper = 0
    lower = 0

    for i in range(len(str)):

        if(str[i] >= 'a' and str[i] <= 'z'):
            lower += 1

        elif(str[i] >= 'A' and str[i] <= 'Z'):
            upper += 1
    return upper, lower


str = input('Masukkan Kalimat yang ingin dihitung: ')
upper_result, lower_result = check_upper_lower(str)

print('Jumlah huruf lower case : ', lower_result)
print('Jumlah huruf upper case : ', upper_result)
