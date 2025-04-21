def input_angka(pesan, tipe=float):
    while True:
        nilai = input(pesan).strip()
        if not nilai:
            print("⚠️  Input tidak boleh kosong!\n")
            continue
        try:
            hasil = tipe(nilai)
            return hasil
        except ValueError:
            tipe_nama = 'bilangan bulat' if isinstance(tipe(), int) else 'angka'
            print(f"❌ Input harus berupa {tipe_nama}!\n")

while True:
    print("🎯==============================🎯")
    print("     KALKULATOR SEDERHANA 🧮")
    print("🎯==============================🎯")
    print("1️⃣  Hitung Luas Segitiga 🔺")
    print("2️⃣  Hitung Luas Persegi Panjang ⬛")
    print("3️⃣  Tentukan Ganjil / Genap 🔢")
    print("4️⃣  Keluar 🚪")
    print("==================================")

    pilihan = input("👉 Pilih menu (1-4): ").strip()

    if not pilihan:
        print("⚠️  Pilihan tidak boleh kosong!\n")
        continue

    if pilihan == '1':
        print("\n🔺 [Luas Segitiga]")
        alas = input_angka("📐 Masukkan alas: ")
        tinggi = input_angka("📏 Masukkan tinggi: ")
        luas = 0.5 * alas * tinggi
        print(f"✅ Luas segitiga = {luas}\n")

    elif pilihan == '2':
        print("\n⬛ [Luas Persegi Panjang]")
        panjang = input_angka("📏 Masukkan panjang: ")
        lebar = input_angka("📐 Masukkan lebar: ")
        luas = panjang * lebar
        print(f"✅ Luas persegi panjang = {luas}\n")

    elif pilihan == '3':
        print("\n🔢 [Cek Ganjil / Genap]")
        angka = input_angka("🎲 Masukkan angka: ", int)
        if angka % 2 == 0:
            print(f"✅ {angka} adalah bilangan **Genap** ✨\n")
        else:
            print(f"✅ {angka} adalah bilangan **Ganjil** 🎯\n")

    elif pilihan == '4':
        print("\n👋 Terima kasih telah menggunakan aplikasi ini. Sampai jumpa lagi!, Develop by : Rifaldi")
        break

    else:
        print("❗ Pilihan tidak valid! Masukkan angka 1 sampai 4.\n")
