inputUang = int(input('Masukan Jumlah Uang Anda: '))
harga = int(input('Masukan Harga Barang: '))
jumlahBarang = int(input('Masukan Jumlah Barang: '))

list_uang = [50000, 20000, 10000, 5000, 2000, 1000, 500, 100]

result = None
total = harga * jumlahBarang
kembalianAsli = inputUang - total
kembalian = inputUang - total
hasil = {}

if kembalian < 0:
    result = 'Uang Anda Tidak Mencukupi'
elif kembalian > 0:
    for item in list_uang:
        if(kembalian >= item):
            a = int(kembalian / item)
            kembalian = kembalian - item
            hasil.update({item :a})
            result = f'Kembalian: {kembalianAsli} ({hasil})'
else:
    result = 'Kembalian: 0'

if result is not None:
    print(result)