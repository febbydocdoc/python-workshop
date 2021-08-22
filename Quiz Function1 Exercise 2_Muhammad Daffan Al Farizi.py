string = input('Masukkan Kalimat yang ingin dihitung: ')
count1 = 0
count2 = 0
for i in string:
    if(i.islower()):
        count1 = count1+1
    elif(i.isupper()):
        count2 = count2+1
print("Jumlah huruf lowercase : ")
print(count1)
print("Jumlah huruf uppercase : ")
print(count2)
