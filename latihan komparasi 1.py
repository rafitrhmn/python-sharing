 #latihan
"""
    TRUE jika agka bernilai 0 samapi 5 dan 8 sampai 11. false jika angka bernilai lain daripada itu
""" 
angka = int(input('masukkaan angka bernilai 0 sampai 5 atau 8 sampai 11???'))

lebih_dari_0 = angka> 0
kurang_dari_5 = angka <5
lebih_dari_8 = angka > 8
kurang_dari_11 = angka < 11


hasil = lebih_dari_0 and kurang_dari_5
hasil_2 = lebih_dari_8 and kurang_dari_11
hasil_akhir = hasil or hasil_2

print(f'angka anda yang bernilai {angka} dinyatakan {hasil_akhir}')