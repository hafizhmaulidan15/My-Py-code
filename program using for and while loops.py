#Buatlah program dengan menggunakan perulangan for dan while yang akan menghasilkan output seperti : 2, 4, 6,8, 10, 12,14,16,18,20
print("perulangan dengan for")
x = int(input("masukan nilai x:"))
for i in range(x,21,2): 
    print (i, end = ' ')
print('\n')

print("---------------------------------------------------")
print("perulangan dengan while")
y = int(input("masukan nilai y:"))
i=y
while i<=20:
    print(i, end = ' ')
    i = i+2
