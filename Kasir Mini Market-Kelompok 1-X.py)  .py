#membuat daftar barang
def daftar_barang():
    print("-----------------------------SELAMAT DATANG-----------------------------")

    print("Toko Utama")
    print("-----------------------------------------------------------------------------")
    print("| No.|Nama Produk | Harga Barang | Jumlah Stok | Kode Unik | kategori       |")
    print("-----------------------------------------------------------------------------")
    print("| 1. |   Coklat   |  Rp. 10.000  |      25     |    ck     | Makanan berat  |")
    print("| 2. |    Kue     |  Rp. 25.000  |      15     |    ke     | Makanan berat  |")
    print("| 3. |   Citato   |  Rp. 18.500  |      10     |    ctt    | Makanan ringan |")
    print("| 4. |   Wafer    |  Rp. 15.000  |      20     |    wfr    | Makanan ringan |")
    print("-----------------------------------------------------------------------------")

#memasukkan jumlah pembelian
daftar_barang()
nama = input("Masukan Tanggal pembelian :")
def garis():
    print("------------------------------------------------------------------------")
garis()
jumlah_beli = int(input("Masukan jumlah transaksi :"))#memasukan jumlah transaksi yang dilakukan pembeli
nama_produk=[]
jumlah_stok=[]
kode_unik=[]
kategori=[]
masukan_jumlah=[]
total_belanja=[]
uang_bayar=[]
uang_kembali=[]
harga=[]
jumlah=[]
i = 0

#pengulangan program dengan syarat dan kondisi tertentu
while i<jumlah_beli : 
    print("Data ke -",i+1)
    
#menambahkan suatu objek
    kode_unik.append(input("Masukan Kode Unik :"))
    masukan_jumlah.append(int(input("Masukan Jumlah Beli :")))
    if kode_unik[i] == "ck":
        nama_produk.append("Coklat")
        kategori.append("makanan berat")
        harga.append("Rp.10000")
        jumlah.append(masukan_jumlah[i]*int("10000"))
    elif kode_unik[i] == "ke":
        nama_produk.append("Kue")
        kategori.append("makanan berat")
        harga.append("Rp.25000")
        jumlah.append(masukan_jumlah[i]*int("25000"))
    elif kode_unik[i] == ("ctt"):
        nama_produk.append("Citato")
        kategori.append("makanan ringan")
        harga.append("Rp.18500")
        jumlah.append(masukan_jumlah[i]*int("18500"))
    elif kode_unik[i] == ("wfr"):
        nama_produk.append("Wafer")
        kategori.append("makanan ringan")
        harga.append("Rp.15000")
        jumlah.append(masukan_jumlah[i]*int("15000"))
    else :
        nama_produk.append("Kode Salah")
        kategori.append("tidak ada")
        harga.append("0")
        jumlah.append(masukan_jumlah[i]*int("0"))
    i = i+1
    
#membuat hasil struk dari pembelian
garis()
print("Tanggal  :", nama )
def daftar_barang():
    print("--------------------------------------------------------------------------")
    print("No  |  Nama produk  |    Harga    |  Qty  | subtotal |      kategori     |")
    print("--------------------------------------------------------------------------")
daftar_barang()
total_belanjaan=0
a = 0

while a<jumlah_beli:
    total_belanja = jumlah[a]+jumlah[a]
    #fungsi %s pemanggilan string yang tidak ada penjumlahan, %i untuk pemanggilan yang akan dijumlahkan
    print("%i       %s         %s      %i       %i       %s"%(a+1, nama_produk[a], harga[a], masukan_jumlah[a], jumlah[a], kategori[a]))
    a = a+1
garis()
print("         Total belanja Rp.", total_belanja)
bayar = int(input("Masukkan uang bayar Rp."))
uang_kembali = bayar-total_belanja
print("         Uang Kembali Rp.", uang_kembali)
