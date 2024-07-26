#4. Buatlah Program untuk menentukan apakah sebuah bangun datar yang memiliki 4 sisi merupakan bujur sangkar atau bukan dengan ketentuan sebagai berikut!
#--- Pengguna diminta untuk memasukkan 4 inputan berupa besaran masing-masing sisi dari bangun datar (misal input sisi 1 = 12, input sisi 2 = 12, input sisi 3 = 12, input sisi 4 = 12)
#--- Jika seluruh inputan bernilai sama antara 1 inputan dengan inputan yang lain, maka berikan keterangan bahwa bangun datar tersebut merupakan "Bujur Sangkar" (misal input sisi 1 = 12, input sisi 2 = 12, input sisi 3 = 12, input sisi 4 = 12, output = "Bujur Sangkar")
#--- Jika tidak maka berikan keterangan bahwa bangun datar tersebut merupakan "Bukan Bujur Sangkar"

sisi1,sisi2,sisi3,sisi4 = input('masukan nilai sisi (beritanda koma) :').split(',')

sisi_1 = float(sisi1)
sisi_2 = float(sisi2)
sisi_3 = float(sisi3)
sisi_4 = float(sisi4)

if sisi_1==sisi_2==sisi_3==sisi_4:
    print("bujur sangkar")
else:
    print("bukan bujur sangkar")