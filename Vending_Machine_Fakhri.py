#vending machine
#M Fakhri Setyabudi

#dictionary nominal-nominal dari kembalian
nominal = {50000: 0, 20000: 0, 10000: 0, 5000: 0, 2000: 0, 1000: 0, 500: 0, 100: 0}

uang = int(input('jumlah uang: '))
harga = int(input('harga barang: '))
barang = int(input('jumlah barang: '))

kembalian1 = uang - (harga*barang)
kembalian = kembalian1

#menghitung banyaknya lembar uang kembalin tiap nominal
for i in nominal:
    while kembalian >= i:
        kembalian -= i
        nominal[i] += 1

#mengupdate dictionary dengan menghilankan nominal kembalian yang berjumlah 0
print('kembalian sebesar: ', kembalian1,'dengan nominal:')
for key in list(nominal.keys()):
    if nominal[key] == 0:
        del nominal[key]
    else:
        print('Uang Rp.',key,'sebanyak',nominal[key])
