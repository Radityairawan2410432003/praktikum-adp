nilai_angka = {'A': 4.00, 'A-': 3.75, 'B+': 3.50, 'B': 3.00,'B-': 2.75, 'C+': 2.50, 'C': 2.00, 'D': 1.00, 'E': 0.00}

jumlah_mahasiswa = int(input("masukkan jumlah mahasiswa :"))
jumlah_matakuliah = int(input("masukkan jumlah mata kuliah :"))

data_mahasiswa = []
for i in range(jumlah_mahasiswa):
    nama = input(f"masukkan nama mahasiswa ke-{i+1} :")
    nilai_matakuliah = []
    total = 0
    for j in range(jumlah_matakuliah):
        nilai = input(f"  Nilai mata kuliah ke-{j+1} (A, B+, dll): ").upper()
        if nilai in nilai_angka:
            nilai_matakuliah.append(nilai)
            total += nilai_angka[nilai]
        
        else:
            print("  Nilai tidak valid. Coba lagi.")
    ip = total / jumlah_matakuliah
    data_mahasiswa.append([nama, nilai_matakuliah, ip])

# Urutkan berdasarkan IP dari tertinggi ke terendah
data_mahasiswa.sort(key=lambda x: x[2], reverse=True)

# Tampilkan tabel hasil
print("\nTABEL NILAI MAHASISWA")
print("="*50)
print(f"{'Nama':<15}{'Nilai':<25}{'IP':>5}")
print("="*50)
for mhs in data_mahasiswa:
    nilai_str = ', '.join(mhs[1])
    print(f"{mhs[0]:<15}{nilai_str:<25}{mhs[2]:>5.2f}")
