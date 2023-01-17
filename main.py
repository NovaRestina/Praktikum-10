                            #Praktikum 10 Latihan 1
txt = 'Hello World'
print()

# Hitung Jumlah Karakternya
print("--------------------------------------------------------")
print("| Jumlah Karakter                     :",len(txt),"\t\t     |")
print("--------------------------------------------------------")

# Ambil Karakter terakhirnya
print("| Karakter Terakhir                   :",txt[-1],"\t\t     |")
print("-------------------------------------------------------")

# Ambil karakter index ke-2 sampai index ke-4 (llo)
print("| Karakter index ke-2 sampai ke-4    :",txt[2:5],"\t\t |")
print("--------------------------------------------------------")

# Hilangkan spasi pada text tersebut (HelloWorld)
print("| Mehilangkan Spasi                  :",txt.replace(" ",""),"|")
print("---------------------------------------------------------")

# Ubah text menjadi huruf besar
print("| mengubah text menjadi huruf besar  :",txt.upper(),"|")
print("------------------------------------------------------")

# Ubah text menjadi huruf kecil
print("| Mengubah text menjadi huruf kecil  :",txt.lower(),"|")
print("------------------------------------------------------")

# Ganti karakter H dengan karakter J
print("| Mengganti karakter H dengan J      :",txt.replace("H","j"),"|")
print("----------------------------------------------------------")



                    # Latihan 2
umur = 24
txt = "Hello, nama saya john, dan umur saya adalah {} tahun"

print(txt.format(umur))