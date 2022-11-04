#latihan komparasi 2 if,else
#latihan 2
"""
    BENAR jika angka kurang dari 0, angka 5 sampai 8 dan lebih
    dari angka 11. SALAH jika angka bernilai 0-5 dan angka 8-11
"""
angka = int(input('masukkan angka kurang 0 atau angka 5 sampai 8 atau angka lebih dari 11?'))

if angka < 0 :
    print(f'angka {angka} yang anda pilih BENAR')
elif angka > 5 and angka < 8  :
    print(f'angka {angka} yang anda pilih BENAR')
elif angka > 11:
    print(f'angka {angka} yang anda pilih BENAR')
else:
    print(f'angka {angka} anda SALAH ') 
