import math # tambah ini paling atas
from datetime import datetime  

print("MESIN PARKIR RIFATH")
sekarang = datetime.now()
print(f"{sekarang.strftime('%A, %d-%m-%Y %H:%M:%S')}")
jam_masuk = float(input("Jam Masuk : ")) # ganti int dengan float supaya bisa input jam dengan menit, contoh: 8.30
jam_keluar = float(input("Jam Keluar : ")) 
selisih_jam = (jam_keluar - jam_masuk) 

# kalo parkir 0 jam, tetap hitung 1 jam
# 1. bulatkan ke atas pake math.ceil() supaya misal parkir 1.5 jam jadi dihitung 2 jam
selisih_jam = math.ceil(selisih_jam)
if selisih_jam <= 0:
    selisih_jam = 1

# logika baru disini
if selisih_jam == 1:
    tarif = 2000  # jam pertama doang
else:
    tarif = 2000 + (selisih_jam - 1) * 1000 # jam pertama 2000, jam selanjutnya 1000/jam

print(f"Total Parkir: {selisih_jam} jam")
print(f"Tarif Parkir: Rp {tarif}")

# 2. Simpan ke file .txt - ini kodenya
with open("laporan_parkir.txt", "a") as f:
    f.write("STRUK PARKIR RIFATH\n")
    f.write(f"{sekarang.strftime('%A, %d-%m-%Y %H:%M:%S')}\n")
    f.write(f"Jam Masuk : {jam_masuk}\n")
    f.write(f"Jam Keluar : {jam_keluar}\n")
    f.write(f"Total Parkir: {selisih_jam} jam\n")
    f.write(f"Tarif Parkir: Rp {tarif}\n")

print("Struk parkir berhasil disimpan ke struk_parkir.txt")