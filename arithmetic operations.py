# operasi aritmatika +, -, /, *, **, %, //
from os import X_OK


a= 25
b=5

#operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

#operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

#operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

#operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

#operasi modulus (sisa dari hasil pembagian) %
hasil = a % b
print(a, '%', b, '=', hasil)

#operasi floor division atau akar pangkat // (kebalikan dari modulus)
hasil = a // b
print(a, '//', b, '=', hasil)


# prioritas operasi, operationaal predecence

'''
    1. ()
    2. exponen
    3. perkalian dan teman - teman nya (*,/,**,//,%)
    pertambahan dan pengurangan + -
'''
a = 98
b = 42
c  = 56

hasil= a**b+a/c*a//b%c/b-a/c
print('hasil dari ini adalah',a,'**',b,'+',a,'/',c,'*',a,'//',b,'%',c,'/',b,'-',a,'/',c, '=', hasil)