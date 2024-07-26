def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Rekursif memanggil sudut masing2
        mergeSort(left)
        mergeSort(right)

        # Dua iterator untuk melintasi dua bagian
        i = 0
        j = 0

        # Iterator untuk list utama
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # Nilai dari setengah kiri sudah terpakai
              myList[k] = left[i]
              # pindahkan iterator ke depan
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # pindahkan ke slot selanjutnya
            k += 1

        # Untuk semua nilai
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [17,83,37,6,10,82,5,11,1]
mergeSort(myList)
print(myList)
