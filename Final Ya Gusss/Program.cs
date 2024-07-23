using System;
using System.Collections.Generic;

class Figure
{
    public string Kode { get; set; }
    public string Nama { get; set; }
    public decimal Harga { get; set; }

    public Figure(string kode, string nama, decimal harga)
    {
        Kode = kode;
        Nama = nama;
        Harga = harga;
    }
}

class TokoFigure
{
    private Dictionary<string, Figure> figures;

    public TokoFigure()
    {
        figures = new Dictionary<string, Figure>
        {
            { "01", new Figure("01", "Kafka", 1200000) },
            { "02", new Figure("02", "Silver Wolf", 1250000) },
            { "03", new Figure("03", "Blade", 1150000) },
            { "04", new Figure("04", "Caelus", 1100000) },
            { "05", new Figure("05", "Bronya", 1175000) },
            { "06", new Figure("06", "Seele", 1275000) },
            { "07", new Figure("07", "Stelle", 1050000) },
            { "08", new Figure("08", "Fu Xuan", 1300000) },
            { "09", new Figure("09", "March 7th", 1375000) },
            { "10", new Figure("10", "Dan Heng", 1350000) },
            { "11", new Figure("11", "Ting Yun", 1230000) },
            { "12", new Figure("12", "Jing Liu", 1400000) },
            { "13", new Figure("13", "Topaz", 1425000) },
            { "14", new Figure("14", "Gepard", 1325000) }
        };
    }

    public void TampilkanDaftarFigure()
    {
        Console.WriteLine("========Daftar Figure========");
        Console.WriteLine("|NO| Nama Figure   | Harga Figure     |");
        Console.WriteLine("--------------------------------------");
        foreach (var figure in figures)
        {
            Console.WriteLine($"|{figure.Value.Kode}| {figure.Value.Nama.PadRight(14)} | Rp {figure.Value.Harga:N2}".PadRight(18) + " |");
        }
        Console.WriteLine("--------------------------------------");
    }

    public Figure CariFigureByKode(string kode)
    {
        figures.TryGetValue(kode, out Figure figure);
        return figure;
    }

    public decimal ProsesPembayaran(Dictionary<Figure, int> keranjangBelanja)
    {
        decimal totalHarga = 0;
        foreach (var item in keranjangBelanja)
        {
            totalHarga += item.Key.Harga * item.Value;
        }
        return totalHarga;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("========Selamat Datang Di Trail Blaze Figure Store========");

        TokoFigure toko = new TokoFigure();
        Dictionary<Figure, int> keranjangBelanja = new Dictionary<Figure, int>();
        string namaPelanggan = "";

        while (true)
        {
            toko.TampilkanDaftarFigure();
            Console.WriteLine("====================Selamat Berbelanja====================");
            Console.Write("Namanya Siapa kak  : ");
            namaPelanggan = Console.ReadLine();
            Console.Write("Masukkan Kode Barang : ");
            string kodeFigure = Console.ReadLine();
            Console.Write("Beli Berapa : ");
            int jumlahFigure = int.Parse(Console.ReadLine());

            Figure figure = toko.CariFigureByKode(kodeFigure);
            if (figure != null)
            {
                if (keranjangBelanja.ContainsKey(figure))
                {
                    keranjangBelanja[figure] += jumlahFigure;
                }
                else
                {
                    keranjangBelanja[figure] = jumlahFigure;
                }
            }
            else
            {
                Console.WriteLine("Barang Tidak Terdaftar");
            }

            Console.Write("Beli Barang Lain ?\tTekan (Yes/No) : ");
            string beliBarangLain = Console.ReadLine();
            if (beliBarangLain.ToLower() == "no")
            {
                break;
            }
        }

        decimal totalPembayaran = toko.ProsesPembayaran(keranjangBelanja);

        Console.WriteLine("========================Detail Pembayaran====================");
        Console.WriteLine("Nama Pelanggan           : " + namaPelanggan);
        Console.WriteLine("Barang yang dipesan      :");
        foreach (var item in keranjangBelanja)
        {
            Console.WriteLine($"   - {item.Key.Nama} ({item.Value} pcs)");
        }
        Console.WriteLine("Total Biaya              : Rp " + totalPembayaran.ToString("N2"));
        Console.Write("Uangnya Kak = ");
        decimal uangPelanggan = decimal.Parse(Console.ReadLine());
        decimal kembalian = uangPelanggan - totalPembayaran;
        if (kembalian >= 0)
        {
            Console.WriteLine("Kembalian                : Rp " + kembalian.ToString("N2"));
            Console.WriteLine("====================Arigatou Gozaimasu, Matakitene================");
        }
        else
        {
            Console.WriteLine("Uang yang diberikan kurang, mohon bayar dengan nominal yang cukup.");
        }
    }
}