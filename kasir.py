print("====== APLIKASI KASIR RESTORAN ======")
total = 0

while True:
    print("\n===== MENU MAKANAN =====")
    print("1. Nasi Goreng - Rp.25.000")
    print("2. Mie Ayam    - Rp.15.000")
    print("3. Ayam Geprek - Rp.20.000")
    print("4. Sate Ayam   - Rp.30.000")
    print("5. Bakso       - Rp.18.000")
    print("0. Selesai Memilih")

    pilihan = int(input("Pilih Menu (0-5): "))

    if pilihan == 0:
        break

    elif pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000

    elif pilihan == 2:
        nama = "Mie Ayam"
        harga = 15000

    elif pilihan == 3:
        nama = "Ayam Geprek"
        harga = 20000

    elif pilihan == 4:
        nama = "Sate Ayam"
        harga = 30000

    elif pilihan == 5:
        nama = "Bakso"
        harga = 18000

    else:
        print("Pilihan Tidak Tersedia!")
        continue

    jumlah = int(input("Masukkan jumlah pesanan: "))

    subtotal = harga * jumlah
    total = total + subtotal

    print("Menu:", nama)
    print("Subtotal: Rp", subtotal)
    print("Total sementara: Rp", total)

#menghitung diskon
if total > 200000:
    diskon = 0.20
else:
    diskon = 0

potongan = total * diskon
total_bayar = total - potongan

#menampilkan struk
print("\n===== STRUK PEMBAYARAN =====")
print("Total Belanja : Rp", total)
print("Diskon        :", int(diskon * 100), "%")
print("Potongan      : Rp", int(potongan))
print("Total Bayar   : Rp", int(total_bayar))
print("=========================================")
print("Terima kasih telah berbelanja!")