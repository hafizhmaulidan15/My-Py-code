print(abs(-19))
# abs() adalah nilai absolut

print(chr(26))
# chr() adalah merubah kode aski dengan karakter

a= [5,6,7,8,9] #menggunakan list atau tupel
b=[2,3,4,5,6,7]
print(sum(a + b,2 )) #cuma bisa di tambah
# sum(iterable, start) bisa digunakan untuk literator variabel
# iterable = memerlukan urutan penjumlahan
# start = opsional, Nilai A yang ditambahkan ke nilai pengembalian/ mmemulai di hitung dari mana


def med3bil(a,b,c,d,e):
    x = [a,b,c,d,e]
    x.sort()
    n = len(x)
    tengah = n % 2
    print("Datanya adalah: ", x)
    return x[tengah]

a,b,c,d,e = input("Masukkan 5 angka bebas (pisahkan dengan koma) : ").split(",")
print("Median : ", med3bil(a,b,c,d,e))

import statistics

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []

# konversi inputan ke dalam list yg berisi integer
for bilangan in inputan.split(','):
    data.append(int(bilangan))

rerata = statistics.mean(data)
print(f'Data -> {data}')
print(f'Mean -> {rerata}')

import statistics

def median():
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print('Median data adalah ', median)
    return