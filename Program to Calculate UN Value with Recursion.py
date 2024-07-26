def Un(n):
    if n == 1:
        return 4
    if n == 2:
        return 7
    else :
        return Un (n-1) + Un (n-2)

print (Un(6))
print (Un(7))
print (Un(8))
