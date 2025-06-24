from collections import deque

# Tuple layanan laundry dan estimasi waktu pengerjaan (dalam jam)
layanan_laundry = (
    ("Cuci Kering", 6),
    ("Cuci Setrika", 8),
    ("Setrika Saja", 4),
    ("Express 3 Jam", 3)
)

# Queue untuk antrian laundry
antrian_laundry = deque()

# Riwayat layanan
riwayat_laundry = []

# Statistik layanan
statistik_laundry = {
    "total_pelanggan": 0,
    "total_jam": 0
}

# Fungsi untuk menampilkan daftar layanan
def tampilkan_layanan():
    print("\nJenis Layanan Laundry:")
    for i, (nama, durasi) in enumerate(layanan_laundry):
        print(f"  {i+1}. {nama} ({durasi} jam)")

# Fungsi menghitung estimasi waktu tunggu
def estimasi_waktu(antrian):
    total_jam = 0
    for data in antrian:
        for layanan in data['layanan']:
            for nama, durasi in layanan_laundry:
                if layanan == nama:
                    total_jam += durasi
    return total_jam

# Fungsi untuk menghitung durasi layanan yang dipilih
def hitung_durasi_layanan(layanan_dipilih):
    return sum([durasi for nama, durasi in layanan_laundry if nama in layanan_dipilih])

# Prosedur untuk mendaftarkan pelanggan ke antrian
def daftar_pelanggan():
    print("\n=== Pendaftaran Pelanggan ===")
    nama = input("Nama Pelanggan: ")
    alamat = input("Alamat: ")
    no_hp = input("Nomor HP: ")
    tampilkan_layanan()
    pilihan = input("Pilih layanan (contoh: 1,3): ").split(',')
    layanan_dipilih = []

    for p in pilihan:
        index = int(p.strip()) - 1
        if 0 <= index < len(layanan_laundry):
            layanan_dipilih.append(layanan_laundry[index][0])

    pelanggan = {
        'nama': nama,
        'alamat': alamat,
        'no_hp': no_hp,
        'layanan': layanan_dipilih
    }

    antrian_laundry.append(pelanggan)
    print(f"Pelanggan {nama} berhasil ditambahkan ke antrian.")

# Prosedur untuk memproses satu pelanggan dari antrian
def proses_laundry():
    if not antrian_laundry:
        print("\nTidak ada pelanggan dalam antrian.")
        return

    pelanggan = antrian_laundry.popleft()
    print("\n=== Proses Laundry ===")
    print(f"Nama        : {pelanggan['nama']}")
    print(f"Alamat      : {pelanggan['alamat']}")
    print(f"No. HP      : {pelanggan['no_hp']}")
    print(f"Layanan     : {', '.join(pelanggan['layanan'])}")
    total_durasi = hitung_durasi_layanan(pelanggan['layanan'])
    print(f"Estimasi waktu pengerjaan: {total_durasi} jam")

    input("Tekan ENTER jika proses selesai...")

    riwayat_laundry.append(pelanggan)
    statistik_laundry['total_pelanggan'] += 1
    statistik_laundry['total_jam'] += total_durasi

    print(f"Laundry untuk {pelanggan['nama']} selesai diproses.\n")

# Prosedur untuk menampilkan antrian saat ini
def tampilkan_antrian():
    if not antrian_laundry:
        print("\nAntrian kosong.")
        return

    print("\n=== Antrian Laundry Saat Ini ===")
    for i, pelanggan in enumerate(antrian_laundry):
        print(f"{i+1}. {pelanggan['nama']} - {pelanggan['alamat']} ({pelanggan['no_hp']})")
        print(f"    Layanan: {', '.join(pelanggan['layanan'])}")
    estimasi = estimasi_waktu(antrian_laundry)
    print(f"\nEstimasi Total Waktu Tunggu: {estimasi} jam")

# Prosedur untuk menampilkan riwayat layanan
def tampilkan_riwayat():
    if not riwayat_laundry:
        print("\nBelum ada pelanggan yang selesai diproses.")
        return

    print("\n=== Riwayat Layanan ===")
    for i, pelanggan in enumerate(riwayat_laundry):
        print(f"{i+1}. {pelanggan['nama']} - {pelanggan['alamat']} ({pelanggan['no_hp']})")
        print(f"    Layanan: {', '.join(pelanggan['layanan'])}")

# Prosedur untuk menampilkan statistik layanan
def tampilkan_statistik():
    print("\n=== Statistik Layanan Laundry ===")
    print(f"Total pelanggan dilayani : {statistik_laundry['total_pelanggan']}")
    print(f"Total waktu pengerjaan   : {statistik_laundry['total_jam']} jam")
    if statistik_laundry['total_pelanggan'] > 0:
        rata2 = statistik_laundry['total_jam'] / statistik_laundry['total_pelanggan']
        print(f"Rata-rata waktu per pelanggan: {rata2:.2f} jam")

# Menu utama aplikasi
def menu():
    while True:
        print("\n===== SISTEM ANTRIAN LAUNDRY (IPA) =====")
        print("1. Daftarkan Pelanggan")
        print("2. Tampilkan Antrian")
        print("3. Proses Laundry Berikutnya")
        print("4. Riwayat Layanan")
        print("5. Statistik Layanan")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            daftar_pelanggan()
        elif pilihan == '2':
            tampilkan_antrian()
        elif pilihan == '3':
            proses_laundry()
        elif pilihan == '4':
            tampilkan_riwayat()
        elif pilihan == '5':
            tampilkan_statistik()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan SIALAU.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
menu()
