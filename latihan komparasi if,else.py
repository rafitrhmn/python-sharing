#latihan komparasi/logika menggunakan if,else (feat.krisna)

"""
    BENAR jika angka bernilai 0 sampai 5 dan 8 sampai 11. SALAH
    jika bukan angka selain itu.
"""

angka = int(input('masukkan angka bernilai 0 sampai 5 atau 8 sampai 11?'))

if angka > 0 and angka < 5:
    print(f'pilhan angka {angka}...benar')
elif angka > 8 and angka < 11:
    print(f'pilhan angka {angka}...benar')
else:
    print(f'mohon maaf angka {angka} salah')

   

