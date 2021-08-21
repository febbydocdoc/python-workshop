#cek palindrom
#M Fakhri Setyabudi

kata = input('masukan kata: ')

reverse = ''.join(reversed(kata))

print(''.join(reversed(kata)))

if kata == reverse:
    print(kata,'adalah palindrom')
else:
    print(kata,'bukan palindrom')
