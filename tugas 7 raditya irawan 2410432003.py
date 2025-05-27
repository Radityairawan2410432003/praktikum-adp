def hitung_glbb(v_awal, a, t):
    v_akhir = v_awal + a * t
    jarak = v_awal * t + 0.5 * a * t * t
    return v_akhir, jarak

n = int(input("masukkan jumlah data (n): "))

hasil = []

for i in range(n):
    print(f"data ke-{i+1}")
    v_awal = float(input("masukan kecepatan awal (m/s): "))
    a = float(input("masukan percepatan (m/s^2): "))
    t = float(input("masukan waktu (s): "))

    v_akhir, jarak = hitung_glbb(v_awal, a, t)
    hasil.append([i+1, v_awal, a, t, v_akhir, jarak])

print("hasil perhitungan Gerak Lurus Berubah Beraturan (GLBB): ")
print("================================================================================")
print("| No | Kecepatan Awal | Percepatan | Waktu | Kecepatan Akhir | Jarak Tempuh    |")
print("================================================================================")

for data in hasil:
    no, v_awal, a, t, v_akhir, jarak = data 
    print(f"| {no:<2} | {v_awal:<14} | {a:<10} | {t:<5} | {v_akhir:<15} | {jarak:<14} |") 

print("================================================================================")