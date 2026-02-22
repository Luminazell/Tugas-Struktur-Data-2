def buku_telepon():
    kontak = {}

    while True:
        pilihan = input("\nTambah (t) | Cari (c) | Tampil (l) | Keluar (k): ").lower()

        if pilihan == "t":
            nama = input("Nama: ")
            nomor = input("Nomor: ")
            kontak.update({nama: nomor})
            print("✔ Kontak ditambahkan")

        elif pilihan == "c":
            nama = input("Nama yang dicari: ")
            print(kontak.get(nama, "✖ Kontak tidak ditemukan"))

        elif pilihan == "l":
            for nama in kontak:
                print(f"{nama} -> {kontak[nama]}")
            if not kontak:
                print("Belum ada kontak.")

        elif pilihan == "k":
            break

        else:
            print("Pilihan salah!")

# Jalankan:
buku_telepon()