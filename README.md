# Praktikum-10

Nama    : Nova Restina Maharani
Kelas   : TI.22.B2
NIM     : 312210525

# Python String

## 1. Latihan 

txt = 'Hello World'

• Hitung jumlah karakternya
• Ambil karakter terakhir
• Ambil karakter index ke-2 sampai index ke-4 (llo)
• Hilangkan spasi pada text tersebut (HelloWorld)
• Ubah text menjadi huruf besar
• Ubah text menjadi huruf kecil
• Ganti karakter H dengan karakter J


## Penjelasan latihan 1

![Screenshot (41)](https://user-images.githubusercontent.com/115637858/212926950-ce11310c-0bd0-4f8d-959d-a07894eaf19e.png)

 1. Hitung Jumlah Karakter pada string menggunakan fungsi len(). Fungsi Len() pada python digunakan untuk menghitung jumlah karakter pada string.

     > print(len(txt))

2. Ambil Karakter terakhir menggunakan index [-1].

    > print(txt[-1])

3. Jika ingin mengambil karakter index ke-2 sampai index ke-4 menggunakan kurung siku yang dideklarasikan di nomor array tersebut.

    > print(txt[2:5])

4. Jika inggin menghilangkan spasi pada string menggunkan fungsi replace(). Fungsi replace() adalah bawaan yantersedia dipython,yang bertujuan untuk mengganti kemunculan karakter substring tertentu dalam string dengan karakter substring tertentu.

    > print(txt.replace(" ",""))

5. Mengubah huruf besar menggunakan Fungsi upper(). Fungsi Upper(0) adalah bawaan dari python untuk mengubah string menjadi huruf besar.

    > print(txt.upper())

6. jika ingin mengubah huruf mejadi kecil menggunakan fungsi lower().

    > print(txt.lower())

7. Menggantikan karakter 'H' dengan karakter 'J' menggunkan fungsi replace().

    > print(txt.replace("H","J"))


## Penjelasan Latihan 2

![Screenshot (42)](https://user-images.githubusercontent.com/115637858/212933014-d44d6010-39ae-4916-8ef6-d2e2d5826768.png)

Memmasukkan variable ke dalam string, dengan menambahkan kurung kurawal {} untuk menetapkan variabel yang sudah tertulis.
 
    > umur = 24
    > txt = 'Hello, nama saya john, dan > > umur saya adalah... tahun'
    > print(txt.format(umur))


## Hasil Output

. Latihan 1

![Screenshot (44)](https://user-images.githubusercontent.com/115637858/212934626-20f0edba-1b0d-4cad-9b15-15a30176504e.png)

. Latihan 2 

![Screenshot (43)](https://user-images.githubusercontent.com/115637858/212935132-b055d496-385c-44c0-b9eb-a8a60bb36ce5.png)


# Thank Youu :)


