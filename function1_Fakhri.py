#Hitung Huruf Besar Kecil
#M Fakhri Setyabudi

def hitung_besarkecil(kalimat):
    besar = 0
    kecil = 0
    for i in kalimat:
        if (i>='a'and i<='z'):
            kecil += 1
        if (i>='A'and i<='Z'):
            besar += 1
    print('Banyak nya huruf besar: ',besar)
    print('Banyak nya huruf kecil: ',kecil)

kata = input('Masukan kata/kalimat yang dihitung: \n')
hitung_besarkecil(kata)
