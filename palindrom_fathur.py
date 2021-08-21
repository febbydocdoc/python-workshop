# fathur

kata = input('Masukan kata: ')
kata2 = kata[::-1]
print(kata2)

if kata == kata2:
    print(kata + " = kata yg anda masukan palindrome")
else:
    print(kata + " = Kata yg anda masukan tidak palindrome")
