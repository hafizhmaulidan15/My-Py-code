def fakt(a):
   if a == 1:
      return (a)
   else:
      return (a*fakt(a-1))

bil = int(input("Masukan Bilangan : "))

print("%d! = %d" % (bil, fakt(bil)))



