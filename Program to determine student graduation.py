#3. Buatlah Program untuk menentukan Kelulusan Mahasiswa dengan ketentuan sebagai berikut!
#--- Pengguna diminta untuk memasukkan nilai
#--- Jika nilai lebih besar dari 70 maka berikan keterangan bahwa mahasiswa tersebut "Lulus"
#--- Jika tidak maka berikan keterangan bahwa mahasiswa tersebut "Tidak Lulus"


print ("program kelulusan mahasiswa")
print ("\n")
nilai = float(input("masukan nilai : "))

if nilai > 70 :
    print ("selamat anda lulus !!!!")
else :
    print ("maaf anda tidak lulus :(")