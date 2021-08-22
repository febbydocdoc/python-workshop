#Square number
#M Fakhri Setyabudi

angka = int(input('Masukan angka: '))

for i in range(1,angka+1):
    print(end='\n')
    if i == 1:
        for j in range(1,angka+1):
            print(j, end='')
    elif i == angka:
        for j in range(angka, 0, -1):
            print(j,end='')
    else:
        for j in range(1,angka+1):
            if j == 1:
                print(i,end='')
            elif j == angka:
                print(angka+1-i,end='')
            else:
                print(' ',end='')
