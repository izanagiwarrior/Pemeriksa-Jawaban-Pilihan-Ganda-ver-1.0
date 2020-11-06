print("===================================================")
print("===== Pemeriksa Jawaban Pilihan Ganda ver 1.0 =====")
print("===================================================")
print("                      Pengembang : M. Faiz Triputra\n")
jumlahSoal = int(input("Masukkan Jumlah Soal : "))
daftarJawaban = []
print("\n================== KUNCI JAWABAN ==================\n")
print("""Pada program ini anda bisa copy paste kunci jawaban dengan menurun ataupun di input 1 per 1
contoh :\n
'A
C
D
A
.
.
.
Z'\n""")
for i in range(jumlahSoal):
    kunciJawaban = input("Masukkan Kunci Jawaban dari Soal ke - %d : " %(i+1))
    daftarJawaban.append(kunciJawaban)
Running = True
while Running:
    print("\n================== JAWABAN SISWA ==================\n")
    print("""Pada program ini anda bisa copy paste jawaban siswa dengan menurun ataupun di input 1 per 1
    contoh :\n
    'A
    C
    D
    A
    .
    .
    .
    Z'\n""")
    Benar = 0
    for i in range(jumlahSoal):
        Jawaban = input("Masukkan Jawaban Siswa dari Soal ke - %d : " %(i+1))
        if Jawaban == daftarJawaban[i]:
            Benar += 1
    print("\nHasil :",Benar,"/",len(daftarJawaban))
    print("Nilai :",round(float((Benar/len(daftarJawaban))*100),2))
    Enter = input("\nIngin memeriksa siswa selanjutnya? # Cukup Menekan tombol Enter untuk lanjut, dan ketik 'Exit' untuk keluar dari aplikasi.\n")
    if Enter:
        Running = False

# 082189100482 => Kalau kamu mengerti codingan ini dan mau mengembangkan bersama. Terima Kasih.