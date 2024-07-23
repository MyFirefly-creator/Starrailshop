print("========Selamat Datang Di Trail Blaze Figure Store========")

barang = [] 
harga = [] 
Total= []
total_harga1= 0
total_harga2= 0
total_harga3= 0
total_harga4= 0
total_harga5= 0
total_harga6= 0
total_harga7= 0
total_harga8= 0
total_harga9= 0
total_harga10= 0
total_harga11= 0
total_harga12= 0
total_harga13= 0
total_harga14= 0

while True:
    print("""========Daftar Figure========
    |NO| Nama Figure | Harga Figure |
    ---------------------------------
    |1|   Kafka    | Rp 1.200.000,00 | 
    |2| Silver Wolf| Rp 1.250.000,00 |
    |3|   Blade    | Rp 1.150.000,00 |
    |4|   Caelus   | Rp 1.100.000,00 |
    |5|   Bronya   | Rp 1.175.000,00 |
    |6|   Seele    | Rp 1.275.000,00 |
    |7|   Stelle   | Rp 1.050.000,00 |
    |8|  Fu Xuan   | RP 1.300.000,00 |
    |9| March 7th  | Rp 1.375.000,00 |
    |10| Dan Heng  | Rp 1.350.000,00 |
    |11| Ting yun  | Rp 1.230.000,00 |
    |12| Jing Liu  | Rp 1.400.000,00 |
    |13| Topaz     | Rp 1.425.000,00 |
    |14| Gepard    | Rp 1.325.000,00 |
    ---------------------------------
 """)
    print("====================Selamat Berbelanja====================")
    eak = str(input("Namanya Siapa kak  : "))
    KODE = int(input("Masukkan Kode Barang : "))
    jumlah_Figure = int(input("Beli Berapa : "))

    if KODE == 1:
        barang.append("Kafka")
        harga.append(1200000)
        total_harga1 = jumlah_Figure * 1200000

    elif KODE == 2:
        barang.append("Silver Wolf")
        harga.append(1250000)
        total_harga2 = jumlah_Figure * 1250000

    elif KODE == 3:
        barang.append("Blade")
        harga.append(1150000)
        total_harga3 = jumlah_Figure * 1150000

    elif KODE == 4:
        barang.append("Caelus")
        harga.append(1100000)
        total_harga4 = jumlah_Figure * 1100000

    elif KODE == 5:
        barang.append("Bronya")
        harga.append(1175000)
        total_harga5 = jumlah_Figure * 1175000

    elif KODE == 6:
        barang.append("Seele")
        harga.append(1275000)
        total_harga6 = jumlah_Figure * 1275000

    elif KODE == 7:
        barang.append("Stelle")
        harga.append(1050000)
        total_harga7 = jumlah_Figure * 1050000

    elif KODE == 8:
        barang.append("Fu Xuan")
        harga.append(1300000)
        total_harga8 = jumlah_Figure * 1300000

    elif KODE == 9:
        barang.append("March 7th")
        harga.append(1375000)         
        total_harga9 = jumlah_Figure * 1375000

    elif KODE == 10:
        barang.append("Dan Heng")
        harga.append(1350000)
        total_harga10 = jumlah_Figure * 1350000

    elif KODE == 11:
        barang.append("Ting Yun")
        harga.append(1230000)
        total_harga11 = jumlah_Figure * 1230000

    elif KODE == 12:
        barang.append("Jing Liu")
        harga.append(1400000)
        total_harga12 = jumlah_Figure * 1400000

    elif KODE == 13:
        barang.append("Topaz")
        harga.append(1425000)
        total_harga13 = jumlah_Figure * 1425000

    elif KODE == 14:
        barang.append("Gepard")
        harga.append(1325000)
        total_harga14 = jumlah_Figure * 1325000

    else:
        print("Barang Tidak Terdaftar")

    beli_barang_lain = input("Beli Barang Lain ?\tTekan (Yes/No) : ")
    if beli_barang_lain == "No" :
        print("")
        break
    

total1 = total_harga1 + total_harga2 + total_harga3 + total_harga4 + total_harga5 + total_harga6 + total_harga7 + total_harga8 + total_harga9 + total_harga10 + total_harga11 + total_harga12 + total_harga13 + total_harga14

Barang = (barang)
Harga = (harga)
umb = int(input("Uangnya Kak = "))

Kembalian = umb-total1

Omagad = ("========================Detail Pembayaran====================")
Owh = ("====================Arigatou Gozaimasu,Matakitene================")

if umb>total1:
    print(Omagad)
    print("Nama Pelanggan           : ",eak)
    print("Figure yang dipesan      : ",Barang)
    print("harga per satu Barang    : ",Harga)
    print("Total Biaya              : ",total1)
    print("Jumlah Uang Yang dibayar : ",umb)
    print("Kembalianmu : ",Kembalian)
    print(Owh)

elif umb==total1:
    print(Omagad)
    print("Nama Pelanggan           : ",eak)
    print("Figure yang dipesan      : ",Barang)
    print("harga per satu Barang    : ",Harga)
    print("Total Biaya              : ",total1)
    print("Jumlah Uang Yang dibayar : ",umb)
    print("Uang Anda Pas: ")
    print(Owh)

else:
    print("Duit Kau Kurang ANJ: ",umb-total1)
    