import random

karakter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890<>()%^*&#!;/,.[{]}?"
while 1:
    baris_kata_sandi = int(input('mau berapa digit password mu :'))
    jumlah_kata_sandi = int(input('mau berapa macam hasil kata sandi mu : '))
    for x in range (0, jumlah_kata_sandi):
        kata_sandi = ''
        for x in range(0, baris_kata_sandi):
            password_karakter = random.choice(karakter)
            kata_sandi      = kata_sandi + password_karakter
        print('ini kata sandi nya : ', kata_sandi)