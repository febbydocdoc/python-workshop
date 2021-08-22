str = input('Masukkan Kalimat yang ingin dihitung: ')
upper = 0
lower = 0
for i in range(len(str)):

    if(str[i] >= 'a' and str[i] <= 'z'):
        lower += 1

    elif(str[i] >= 'A' and str[i] <= 'Z'):
        upper += 1
print('Jumlah huruf lower case : ', lower)
print('Jumlah huruf upper case : ', upper)
