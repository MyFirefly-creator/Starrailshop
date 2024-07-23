class ActionFigure:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Gudang:
    def __init__(self):
        self.daftar_action_figure = {
            "01": ActionFigure("Kafka", 1200000, 100),
            "02": ActionFigure("Silver Wolf", 1250000, 100),
            "03": ActionFigure("Blade", 1150000, 100),
            "04": ActionFigure("Caelus", 1100000, 100),
            "05": ActionFigure("Bronya", 1175000, 100),
            "06": ActionFigure("Seele", 1275000, 100),
            "07": ActionFigure("Stelle", 1050000, 100),
            "08": ActionFigure("Fu Xuan", 1300000, 100),
            "09": ActionFigure("March 7th", 1375000, 100),
            "10": ActionFigure("Dan Heng", 1350000, 100),
            "11": ActionFigure("Ting Yun", 1230000, 100),
            "12": ActionFigure("Jing Liu", 1400000, 100),
            "13": ActionFigure("Topaz", 1425000, 100),
            "14": ActionFigure("Gepard", 1325000, 100)
        }

    def tampilkan_daftar_action_figure(self):
        print("Daftar Action Figure di Gudang:")
        print("No. | Nama Action Figure | Harga | Stok")
        print("------------------------------------------")
        for nomor, action_figure in self.daftar_action_figure.items():
            print(f"{nomor}   | {action_figure.nama.ljust(18)} | {action_figure.harga} | {action_figure.stok}")
        print("------------------------------------------")

    def login_admin(self, username, password):
        # Simulasi login admin, return True jika login berhasil, False jika gagal
        if username == "admin" and password == "admin123":
            return True
        else:
            return False

    def tambah_stok_action_figure(self, nomor, jumlah):
        if nomor in self.daftar_action_figure:
            self.daftar_action_figure[nomor].stok += jumlah
            print(f"Stok {self.daftar_action_figure[nomor].nama} berhasil ditambahkan sebanyak {jumlah}. Stok sekarang: {self.daftar_action_figure[nomor].stok}")
        else:
            print("Action figure tidak ditemukan.")

if __name__ == "__main__":
    gudang = Gudang()

    # Login sebagai admin
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if gudang.login_admin(username, password):
            print("Login berhasil!")
            break
        else:
            print("Username atau password salah. Silakan coba lagi.")

    # Tampilkan daftar action figure di gudang
    gudang.tampilkan_daftar_action_figure()

    # Tambah stok action figure jika diizinkan oleh admin
    tambah_stok = input("Apakah Anda ingin menambah stok action figure? (y/n): ")
    if tambah_stok.lower() == 'y':
        nomor = input("Masukkan nomor action figure yang akan ditambah stoknya: ")
        jumlah = int(input("Masukkan jumlah stok yang akan ditambahkan: "))
        gudang.tambah_stok_action_figure(nomor, jumlah)
    else:
        print("Operasi ditutup.")

    # Tampilkan kembali daftar action figure setelah penambahan stok
    gudang.tampilkan_daftar_action_figure()
