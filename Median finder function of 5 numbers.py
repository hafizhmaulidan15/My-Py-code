
def med5bil(a,b,c,d,e):
    #disini kita akan mengubah variabel a,b,c,d,e menjadi 1 variabel yaitu deret\
    deret=[a,b,c,d,e]
    deretsorted=sorted(deret)
    n = len(deretsorted) 
    i_tengah = n // 2 

    if n % 2 == 1:
        return deretsorted[i_tengah]
    return (deretsorted[i_tengah - 1] + deret[i_tengah]) / 2

a,b,c,d,e = input("Masukkan 5 angka dipisah dengan spasi: ").split(' ')
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
print("Median dari ",a,b,c,d,e,"Ialah",med5bil(a,b,c,d,e))
