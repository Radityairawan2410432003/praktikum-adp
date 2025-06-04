data = """\
Wahyu Andani,2410432004,A2,ketua acara,85,Acara
Yazid Riyanda Putra,2410431005,A3,anggota acara,80,Acara
Lala Abdilah Batubara,2410431031,A1,anggota acara,75,Acara
Nur Azizah,2410432011,A1,anggota acara,78,Acara
Muqadis Khairy Yusran,2410433002,A2,ketua pubdok,88,Pubdok
Naila Fariska Azzahra,2410431016,A3,anggota pubdok,80,Pubdok
Muhammad Arifin Ilham,241043100,A2,anggota pubdok,82,Pubdok
Suci Syahira,2410433003,A1,anggota pubdok,79,Pubdok
Muhammad Zhafran Ariella,2410433009,A1,ketua perlengkapan,84,Perlengkapan
Raditya Irawan,2410432003,A1,anggota perlengkapan,80,Perlengkapan
Danda Ahmad Dzaki,2410432030,A3,anggota perlengkapan,76,Perlengkapan
Melda Afrilia,2410432041,A1,anggota perlengkapan,78,Perlengkapan
Fauzi Taufiqurrahman,2410431036,A3,ketua Danus,86,Danus
Dicky Rivaldi Kurniawan,2410432031,A1,anggota Danus,81,Danus
Bima Niskala Lisyanda,2410433015,A3,anggota Danus,79,Danus
Shalsya Adina Marsya,2410432009,A1,anggota Danus,77,Danus
"""

with open("OrPSB22.txt", "w") as file:
    file.write(data)

print("file OrPSB22.txt berhasil dibuat dengan 4 calon per bidang.")

def hitung_poin_pengalaman(teks_pengalaman, bidang_dipilih):
    poin = 0
    teks_pengalaman = teks_pengalaman.lower()
    bidang_dipilih = bidang_dipilih.lower()

    if "ketua" in teks_pengalaman:
        poin += 2
    if bidang_dipilih in teks_pengalaman:
        poin += 3
    return poin

def baca_data():
    with open("OrPSB22.txt", "r") as file:
        baris = file.readlines()

    daftar_calon = []

    for data in baris:
        nama, nim, kelas, pengalaman, nilai_wawancara, bidang = data.strip().split(",")
        nilai_wawancara = int(nilai_wawancara)
        tambahan_nilai = hitung_poin_pengalaman(pengalaman, bidang)
        nilai_akhir = nilai_wawancara + tambahan_nilai

        calon = {
            "nama": nama,
            "nim": nim,
            "kelas": kelas,
            "bidang": bidang,
            "nilai": nilai_akhir
        }
        daftar_calon.append(calon)

    return daftar_calon

def pilih_koordinator(daftar_calon):
    bidang_dic = {}

    for calon in daftar_calon:
        bidang = calon["bidang"]
        if bidang not in bidang_dic:
            bidang_dic[bidang] = []
        bidang_dic[bidang].append(calon)

    hasil = {}

    for bidang in bidang_dic:
        calon_list = bidang_dic[bidang]

        for i in range(len(calon_list)):
            idx_max = i
            for j in range(i +1, len(calon_list)):
                if calon_list[j]["nilai"] > calon_list[idx_max]["nilai"]:
                    idx_max = j
                calon_list[i], calon_list[idx_max] = calon_list[idx_max], calon_list[i]

            if len(calon_list) >= 2:
                hasil[bidang] = [calon_list[0], calon_list[1]]
            elif len(calon_list) == 1:
                hasil[bidang] = [calon_list[0]]

    return hasil

data_calon = baca_data()
hasil_koordinator = pilih_koordinator(data_calon)

print("\nKoordinator Terpilih Tiap Bidang:")
for bidang, dua_teratas in hasil_koordinator.items():
    print(f"\nBidang: {bidang}")
    for calon in dua_teratas:
        print(f"- {calon['nama']} (NIM: {calon['nim']}) - Nilai: {calon['nilai']}")
