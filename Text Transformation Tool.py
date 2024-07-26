def mengecil(data):
    #Memakai sistem data.lower dapat mengubah huruf kecil
    print("Mengubah hurup kecil: ", data.lower())

def membersar(data):
    #Memakai sistem data.upper dapat mengubah huruf menjadi besar
    print("Mengubah hurup besar: ", data.upper())

def hilang(data):
    #Memakai sistem data.replace dapat menghilangkan huruf yang kita inginkan misal 'a'
    print("Menghilangkan huruf a: ", data.replace("a", ""))

print("Pilih parameter")
print('1. memperkecil huruf\n' '2. memberbesar huruf\n' '3. menghilangkan huruf A\n')
pilihan = int(input('Masukkan pilihan anda : '))

if pilihan == 1:
    print('Anda memilih memperkecil huruf')
    b1 = str(input('Masukkan kalimat: '))
    mengecil(b1)

elif pilihan == 2:
    print('Anda memilih memperbesar huruf')
    b1=str(input('Masukan kalimat:'))
    membersar(b1)

elif pilihan == 3:
    print('Anda memilih menghilangkan huruf A')
    b1=str(input('Masukan kalimat: '))
    hilang(b1)
else:
    print('maaf tidak ada pilihan lain')
