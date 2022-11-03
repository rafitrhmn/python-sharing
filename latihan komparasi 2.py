#latihan 2
"""
    TRUE jika angka kurang dari 0, angka 5 sampai 8 dan lebih dari angka 11. FALSE jika angka 0-5dan angka 8-11
"""
angka = int(input('masukkan angka kurang dari 0 atau 5 sampai 8 atau lebih dari 11???...'))

kurang_dari_0 = angka < 0
lebih_dari_5 = angka > 5
kurang_dari_8 = angka < 8
lebih_dari_11 = angka > 11

hasil_1 = kurang_dari_0 or lebih_dari_5
hasil_2 = kurang_dari_8 or lebih_dari_11
hasil_akhir = hasil_1 and hasil_2

print(f'angka anda bernilai {angka} dinyatakan {hasil_akhir}')