print("MESIN PARKIR RIFATH")

jam_masuk = int(input("Jam Masuk : ")) # contoh: ketik 8
jam_keluar = int(input("Jam Keluar : ")) # contoh ketik 11

# Rumus: Tarif = (Jam Keluar - Jam Masuk) x 2000
# Keterangan: 2000 = tarif parkir di jam pertama, jam selanjutnya 1000/jam
selisih_jam = (jam_keluar - jam_masuk) 

# kalo parkit 0 jam, tetap hitung 1 jam
if selisih_jam <= 0:
    selisih_jam = 1

# logika baru disini
if selisih_jam == 1:
    tarif = 2000  # jam pertama doang
else:
    tarif = 2000 + (selisih_jam - 1) * 1000 # jam pertama 2000, jam selanjutnya 1000/jam

print(f"Tarif Parkir: Rp {tarif}")
