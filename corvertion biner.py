from tabulate import tabulate
import itertools as it

def genConverter(angka, pembilang):
    result = []
    loop = True
    while loop:
        if angka > pembilang:
            result.append(angka)
            sisa = angka % pembilang
            angka = angka // pembilang
            if sisa > 9:
                sisa = libChar(sisa)
            divid = "{0}------  {1}".format(pembilang, sisa)
            result.append(divid)
        else:
            if angka > 9:
                angka = libChar(angka)
            result.append(angka)
            loop = False
            break
        result.append("")

    return result

def libChar(angka):
    if angka == 10:
        return "10 = A"
    elif angka == 11:
        return "11 = B"
    elif angka == 12:
        return "12 = C"
    elif angka == 13:
        return "13 = D"
    elif angka == 14:
        return "14 = E"
    elif angka == 15:
        return "15 = F"
    elif angka == 16:
        return "16 = G"

angka = int(input("Masukkan bilangan untuk dikonversi : "))
output = []

biner = genConverter(angka, 2)
octal = genConverter(angka, 8)
hexa = genConverter(angka, 16)


combine = list(it.zip_longest(biner, octal, hexa))


header = ("Binner", "Octal", "Hexadecimal")

print(tabulate(combine, header, tablefmt="plain"))