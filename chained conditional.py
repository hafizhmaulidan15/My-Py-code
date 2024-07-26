#chained conditional
a,b,c,d=input("masukan nilai: ").split(",")
a=float(a)
b=float(b)
c=float(c)
d=float(d)
n=a*0.3+b*0.15+c*0.35+d*0.2
if n >= 90 :
	print("A")
elif 80 <= n < 90 :
	print("B")
elif 70 <= n < 80 :
	print("C")
elif 60 <= n < 70 :
	print("D")
elif n < 60 :
	print("E")
else :
	print("Nilai Salah")
