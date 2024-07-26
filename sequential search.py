list_1 = [17, 83, 37, 6, 10, 82, 5, 11]
x=int(input("masukkan angka :"))
n = len(list_1)
for i in range (0,n):
    if list_1[i] == x:
        print("angka ditemukan")
    elif list_1[i] != x :
        print("angka tidak sama")
        
