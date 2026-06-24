from datetime import datetime
import locale

total_uang = 0
total_jam = 0
jumlah_motor = 0
data_sementara = {} # keranjang buat nampung 1 motor

# 1. Buka file laporan_parkir.txt mode "r" = read/baca
with open ("laporan_parkir.txt", "r") as f:
    for baris in f: # Loop tiap baris
        # baris isinya: "2026-04-19 10:30 | Masuk: 8.0 Keluar: 9.5 | Rp3000"
        baris = baris.strip()
        if not baris: # kalo baris nya kosong skip aja. lanjut baris berikutnya
            continue

        # kalo ketemu "Jam masuk", simpen ke keranjang
        if "Jam Masuk" in baris:
            jam_masuk = float(baris.split(":")[1].strip())
            data_sementara['masuk'] = jam_masuk
            
        # kalo ketemu "Jam keluar", simpen ke keranjang
        if "Jam Keluar" in baris:
            jam_keluar = float(baris.split(":")[1].strip())
            data_sementara['keluar'] = jam_keluar

        # kalo ketemu "Tarif Parkir", berarti 1 motor udah lengkap. tinggal hitung!
        if "Tarif Parkir" in baris:
            tarif = int(baris.split(":")[1].replace("Rp", "").strip())
            data_sementara['tarif'] = tarif

            # Hitung Sekarang!
            lama_parkir = data_sementara['keluar'] - data_sementara["masuk"]
            total_uang = total_uang + tarif
            total_jam = total_jam + lama_parkir
            jumlah_motor = jumlah_motor + 1

            data_sementara = {} # Kosongin keranjang buat motor berikutnya

# 4. Hitung rata-rata
if jumlah_motor > 0:
    rata2_jam = total_jam / jumlah_motor
else:
    rata2_jam = 0

print("===DASHBOARD PARKIR HARI INI===")
sekarang = datetime.now()
print(f"{sekarang.strftime('%A, %d-%m-%Y %H:%M:%S')}")
print(f"Total Motor: {jumlah_motor}")
print(f"Total Pemasukan: Rp {total_uang:,}")
print(f"Rata-rata Lama Parkir: {rata2_jam: .1f} jam")
