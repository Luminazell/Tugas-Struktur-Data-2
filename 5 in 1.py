# ===============================
# PROGRAM LATIHAN SOAL (1–5)
# ===============================

from collections import OrderedDict


# 1. Dedupikasi
def deduplikasi(lst):
    return list(OrderedDict.fromkeys(lst))


# 2. Intersection Dua Array
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


# 3. Anagram Check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# 4. First Recurring Character
def first_recurring_char(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return s[i]
    return None


# 5. Buku Telepon
def buku_telepon():
    kontak = {}

    while True:
        pilihan = input("\nTambah (t) | Cari (c) | Tampil (l) | Keluar (k): ").lower()

        if pilihan == "t":
            nama = input("Nama: ")
            nomor = input("Nomor: ")
            kontak[nama] = nomor
            print("✔ Kontak ditambahkan")

        elif pilihan == "c":
            nama = input("Nama yang dicari: ")
            print(kontak.get(nama, "✖ Kontak tidak ditemukan"))

        elif pilihan == "l":
            if not kontak:
                print("Belum ada kontak.")
            else:
                for nama, nomor in kontak.items():
                    print(f"{nama} -> {nomor}")

        elif pilihan == "k":
            break

        else:
            print("Pilihan salah!")


# ===============================
# MENU UTAMA
# ===============================

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Dedupikasi List")
    print("2. Intersection Dua Array")
    print("3. Cek Anagram")
    print("4. First Recurring Character")
    print("5. Buku Telepon")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        data = list(map(int, input("Masukkan angka (pisahkan spasi): ").split()))
        print("Hasil:", deduplikasi(data))

    elif pilih == "2":
        arr1 = list(map(int, input("Array 1 (pisahkan spasi): ").split()))
        arr2 = list(map(int, input("Array 2 (pisahkan spasi): ").split()))
        print("Hasil:", intersection(arr1, arr2))

    elif pilih == "3":
        s1 = input("String pertama: ")
        s2 = input("String kedua: ")
        print("Anagram?" , is_anagram(s1, s2))

    elif pilih == "4":
        s = input("Masukkan string: ")
        hasil = first_recurring_char(s)
        print("Karakter berulang pertama:", hasil)

    elif pilih == "5":
        buku_telepon()

    elif pilih == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")