##
# Program untuk menentukan apakah sebuah bilangan yang diinput ganjil atau genap
#
# Membaca bilangan yang dimasukkan user
bil = int(input("Masukkan sebuah bilangan:"))
# Proses untuk menentukan bilangan tersebut ganjil atau genap
# Menggunakan operator modulus
if bil % 2 == 1:
  print(bil, "adalah bilangan ganjil")
else:
  print(bil, "adalah bilangan genap")

print("")

##
# Program untuk menentukan apakah huruf tersebut vokal atau konsonan
# Dalam Ejaan Bahasa Inggris
# Membaca huruf yang dimasukkan user
hur= input("Masukkan sebuah huruf dari kumpulan abjad:")
#Proses menentukan huruf dan menampilkan hasilnya
if hur =="a" or hur == "e" or \
   hur =="i" or hur == "o" or \
   hur =="u":
  print("Ini adalah vokal.")
elif hur =="y":
  print("Kadang vokal...kadang konsonan")
else:
  print("Ini adalah konsonan.")

print("")

##
# Menampilkan nama ukuran geometri berdasarkan jumlah sisi yang diinput
#
# Membaca jumlah sisi yang diinput oleh user
sisi = int(input("Masukkan jumlah sisinya:"))
# Menampilkan nama ukuran geometri tersebut
nama = ""
if sisi == 3:
  nama = "triangle"
elif sisi == 4:
  nama = "quadrilateral"
elif sisi == 5:
  nama = "pentagon"
elif sisi == 6:
  nama = "hexagon"
elif sisi == 7:
  nama = "heptagon"
elif sisi == 8:
  nama = "ocatagon"
elif sisi == 9:
  nama = "nonagon"
elif sisi == 10:
  nama = "decagon"
# Menampilkan pesan kesalahan atau nama dari ruang geometri
if nama == "":
  print("Jumlah sisi yang diinput tidak ada dalam database")
else:
  print("Ini adalah", nama)

