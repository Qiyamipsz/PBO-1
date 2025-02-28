##
# Menampilkan alamat lengkap seseorang 
#
print("Hendri Ahmadian")
print("Department of Information Technology")
print("UIN Ar-Raniry")
print("Jalan Syech Abdurrauf Kopelma Darussalam")
print("Banda Aceh 23111")
print("Indonesia")

print("")

##
# Menghitung luas kamar
#
# Membaca angka yang dimasukkan oleh user
panjang = float(input("Masukkan ukuran panjang dalam satuan meter "))
lebar = float(input("Masukkan ukuran lebar dalam satuan meter "))
# Proses perhitungan luas
luas = panjang * lebar
# Tampilkan hasil
print("Luas dari kamar ini adalah", luas, "meter kuadrat")

print("")

##
# Menghitung jumlah dari bilangan positif pertama
#
# Membaca angka yang dimasukkan oleh user
n = int(input("Masukkan bilangan bulat positif:"))
# Proses Menghitung jumlah
sm = n * (n+1) / 2
# Tampilkan hasil
print("Jumlah pertama dari ", n, "bilangan positif adalah", sm)

print("")

## 
# Pengenalan operator matematika pada Python dan modul math
#
from math import log10
# Membaca input dari user
x = int (input("Masukkan bilangan dari x:"))
y = int (input("Masukkan bilangan dari y:"))
# Menghitung dan menampilkan operator matematika
print(x, "+", y, "adalah", x + y)
print(x, "-", y, "adalah", x - y)
print(x, "*", y, "adalah", x * y)
print(x, "/", y, "adalah", x / y)
print(x, "%", y, "adalah", x % y)

# Menghitung logaritma dan pangkat
print("Logaritma basis 10 dari", x, "adalah", log10(x))
print(x, "^", y, "adalah", x**y)


