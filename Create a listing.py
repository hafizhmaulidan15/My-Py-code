#Membuat listing

#inisiasi list
mylist = ["apel", "jeruk", "Mangga", "alpukat", "anggur", "lemon", "kiwi", "sirsak"]

#input list
print("input list : ", end=" ")
for i in mylist:
		print(i, end=",")

#memasukkan item yang kita ambil dari mylist index 2 ke index 0
mylist.insert(0,mylist[2])

#menghapus index ke-3
mylist.pop(3)

#Memasukan item yang diambil dari mylist index 2 kedalam list terakhir
mylist.append(mylist[6])

#Menghapus list index ke 6
mylist.pop(6)

print("\n")
print("list : ", end=" ")
for x in mylist:
		print(x, end=",")
