# fungsi untuk daftar menu makanan
def makanan():
        global total_makan, jumlah_porsi, nama_makanan
        
# fungsi untuk daftar menu minuman
def minuman():
        global total_minum, jumlah_gelas, nama_minuman
        
print("|=================================|")
print("|  Program Mesin Kasir Sederhana  |")
print("|=================================|")
print("|      : Pilih Menu Makanan :     |")
print("|=================================|")
print("| 1. Nasi Goreng        Rp.12000  |")
print("| 2. Ayam Geprek        Rp.15000  |")
print("| 3. Mie Goreng/Rebus   Rp.5000   |")
print("| 4. Ketoprak           Rp.10000  |")
print("| 5. Ikan Bakar         Rp.19000  |")
print("|=================================|")
menu_makanan = int(input(" Pilih Menu (1/2/3/4/5) : "))
jumlah_porsi = int(input(" Berapa Porsi :"))

if menu_makanan == 1:
    total_makan = jumlah_porsi * 12000
    print(" Nasi Goreng",jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = (" Nasi Goreng ")
elif menu_makanan == 2:
    total_makan = jumlah_porsi * 15000
    print(" Ayam Geprek",jumlah_porsi,"Porsi : Rp.", total_makan)
    nama_makanan = (" Ayam Geprek" )
elif menu_makanan == 3:
    total_makan = jumlah_porsi * 5000
    print("Mie Goreng/Rebus",jumlah_porsi,"Porsi : Rp.", total_makan)
    nama_makanan = (" Mie Goreng/Rebus ")
elif menu_makanan == 4:
    total_makan = jumlah_porsi * 10000
    print("Ketoprak",jumlah_porsi,"Porsi Rp.", total_makan)
    nama_makanan = (" Ketoprak ")
elif menu_makanan == 5:
    total_makan = jumlah_porsi * 19000
    print("Ikan Bakar",jumlah_porsi,"Porsi Rp.", total_makan)
    nama_makanan = (" Ikan Bakar ")
else:
    print(" Pilihan Tidak Tersedia ")
    
# Untuk Minuman 
print()
print("|==================================|")
print("|      : Pilih Menu Minuman :      |")
print("|==================================|")
print("| 1. Es Teh/Hangat        Rp.4000  |")
print("| 2. Es Jeruk             Rp.6500  |")
print("| 3. Juz Jeruk            Rp.8000  |")
print("| 4. Juz Alpukat          Rp.10000 |")
print("| 5. Juz Mangga           Rp.11500 |")
print("| 6. Juz Sirsak           Rp.9000  |")
print("| 7. Juz Apel             Rp.10500 |")
print("| 8. Susu hangat/dingin   Rp.8000  |")
print("| 9. Kopi                 Rp.5000  |")
print("| 10. Soda                Rp.11500 |")
print("|==================================|")
menu_minuman = int(input("Pilih Menu 1/2/3/4/5/6/7/8/9/10 : "))
jumlah_gelas = int(input(" Berapa Gelas : "))

if menu_minuman == 1:
    total_minum = jumlah_gelas * 4000
    print("Es Teh/Hangat",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("ES Teh/Hangat")
elif menu_minuman == 2:
    total_minum = jumlah_gelas * 6500
    print("es Jeruk",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Es Jeruk")
elif menu_minuman == 3:
    total_minum = jumlah_gelas * 8000
    print("Juz Jeruk",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Juz Jeruk")
elif menu_minuman == 4:
    total_minum = jumlah_gelas * 10000
    print("Juz Alpukat",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Juz Alpukat")
elif menu_minuman == 5:
    total_minum = jumlah_gelas * 11500
    print("Juz Mangga",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Juz Mangga")
elif menu_minuman == 6:
    total_minum = jumlah_gelas * 9000
    print("Juz Sirsak",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Juz Sirsak")
elif menu_minuman == 7:
    total_minum = jumlah_gelas * 10500
    print("Juz Apel",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Juz Apel")
elif menu_minuman == 8:
    total_minum = jumlah_gelas * 8000
    print("Susu hangat/dingin",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Susu hangat/dingin")
elif menu_minuman == 9:
    total_minum = jumlah_gelas * 5000
    print("Kopi",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Kopi")
elif menu_minuman == 10:
    total_minum = jumlah_gelas * 11500
    print("Soda",jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Soda")
else:
    print(" Pilihan Tidak Tersedia ")
    
# proses menghitung semua harga yang harus dibayar
makanan()
minuman()
jumlah_semuanya = total_makan + total_minum

# daftar pembelian
print()
print("|==================================|")
print("|          Daftar Pembelian        |")
print("|==================================|")
print("| Makanan :",nama_makanan,"\t  |")
print("| Porsi   :",jumlah_porsi,"\t\t\t    |")
print("| Minuman :",nama_minuman,"\t  |")
print("| Gelas   :",jumlah_gelas,"\t\t\t    |")
print("|==================================|")
print("|      Jadi Yang Harus Dibayar     |")
print("|==================================|")
print("| Total :",jumlah_semuanya,"                 |")
print("|==================================|")
print()