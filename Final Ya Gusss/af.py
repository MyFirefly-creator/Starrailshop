import os
class Figure:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga


class TokoFigure:
    def __init__(self):
        self.figures = {
            "01": Figure("01", "Kafka", 1200000),
            "02": Figure("02", "Silver Wolf", 1250000),
            "03": Figure("03", "Blade", 1150000),
            "04": Figure("04", "Caelus", 1100000),
            "05": Figure("05", "Bronya", 1175000),
            "06": Figure("06", "Seele", 1275000),
            "07": Figure("07", "Stelle", 1050000),
            "08": Figure("08", "Fu Xuan", 1300000),
            "09": Figure("09", "March 7th", 1375000),
            "10": Figure("10", "Dan Heng", 1350000),
            "11": Figure("11", "Ting Yun", 1230000),
            "12": Figure("12", "Jing Liu", 1400000),
            "13": Figure("13", "Topaz", 1425000),
            "14": Figure("14", "Gepard", 1325000)
        }

    def tampilkan_daftar_figure(self):
        print("========Daftar Figure========")
        print("|NO| Nama Figure   | Harga Figure     |")
        print("--------------------------------------")
        for kode, figure in self.figures.items():
            print(f"|{kode}| {figure.nama.ljust(14)} | Rp {figure.harga:,.2f}".ljust(18) + " |")
        print("--------------------------------------")

    def cari_figure_by_kode(self, kode):
        return self.figures.get(kode)

    def proses_pembayaran(self, keranjang_belanja):
        total_harga = sum(item.harga * jumlah for item, jumlah in keranjang_belanja.items())
        return total_harga


if __name__ == "__main__":
    print("========Selamat Datang Di Trail Blaze Figure Store========")

    toko = TokoFigure()
    keranjang_belanja = {}

    while True:
        toko.tampilkan_daftar_figure()
        print("====================Selamat Berbelanja====================")
        nama_pelanggan = input("Namanya Siapa kak  : ")
        kode_figure = input("Masukkan Kode Barang : ")
        jumlah_figure = int(input("Beli Berapa : "))

        figure = toko.cari_figure_by_kode(kode_figure)
        if figure:
            keranjang_belanja[figure] = keranjang_belanja.get(figure, 0) + jumlah_figure
        else:
            print("Barang Tidak Terdaftar")

        beli_barang_lain = input("Beli Barang Lain ?\tTekan (Yes/No) : ")
        if beli_barang_lain.lower() == "no":
            break

    total_pembayaran = toko.proses_pembayaran(keranjang_belanja)

    print("========================Detail Pembayaran====================")
    print("Nama Pelanggan           :", nama_pelanggan)
    print("Barang yang dipesan      :")
    for figure, jumlah in keranjang_belanja.items():
        print(f"   - {figure.nama} ({jumlah} pcs)")
    print("Total Biaya              : Rp {:,.2f}".format(total_pembayaran))
    uang_pelanggan = int(input("Uangnya Kak = "))
    kembalian = uang_pelanggan - total_pembayaran
    if kembalian >= 0:
        print("Kembalian                : Rp {:,.2f}".format(kembalian))
        print("====================Arigatou Gozaimasu, Matakitene================")
    else:
        print("Uang yang diberikan kurang, mohon bayar dengan nominal yang cukup.")