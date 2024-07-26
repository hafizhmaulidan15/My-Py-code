#penerapan binary search
# else return -1
def bin_search(list1,n):
	bawah = 0
	atas = len(list1)-1
	tengah = 0
	
	while bawah <= atas:
		#untuk menghasilkan sebuah angka
		tengah =(atas+bawah)//2
		#mengecek jika n berada pada di tengah
		if list1[tengah]<n:
			bawah = tengah + 1 
		#jika n lebih besar, bandingkan ke sisi kanan tengah
		elif list1[tengah]>n:
			atas = tengah - 1	
		#jika n lebih kecil, bandingkan ke sisi kiri tengah
		else:
			return tengah
	#jika elemen tidak ada pada list
	return -1	
#inisial list1	
list1 = [17,83,37,6,10,82,5,11,1]
list1.sort()
n=int(input("masukkan angka :"))	
#memanggil fungsi
hasil = bin_search(list1,n)
	
if hasil != -1:
	print("elemen terdapat pada indeks",str(hasil))
else:
	print("elemen tidak terdapat pada list1")
