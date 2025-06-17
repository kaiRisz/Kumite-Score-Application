import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import csv
import perhitungan

#kelas untuk membuat data base score
class ScoreDatabase:
    def __init__(self):
        self.data = []

    def reset(self):
        self.data = []  
        
    def get_sorted_scores(self):
        sorted_data = self.data.copy()  # Biar data asli gak ikut berubah
        n = len(sorted_data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_data[j]["skor"] < sorted_data[j + 1]["skor"]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        return sorted_data
    
    def tambah_skor(self, nama, skor, division):
        for peserta in self.data:
            if peserta["nama"] == nama:
                peserta["skor"] += int(skor)
                peserta["division"] == division
                return
        self.data.append({"nama": nama, "skor": int(skor), "division": division})

#kelas untuk buat tampilan awal aplikasi
class LoadingPage:
    def __init__(self, root, db):
        self.root = root
        self.db = db

        self.bg_image = Image.open("opening.jpg").resize((1366, 768))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.tombol_mulai = tk.Button(
            self.root, text="CLICK", font=("system", 17, "bold"), width=20, height=2,
            bg="#cfcfcf", fg="black", command=self.buka_menu
        )
        self.tombol_mulai.place(relx=0.5, rely=0.67, anchor="center")

    def buka_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Menu(self.root, self.db)

#kelas untuk nampilin menu yang ada di aplikasi ini
class Menu:
    def __init__(self, root, db):
        self.root = root
        self.db = db

        self.bg_image = Image.open("menu.jpg").resize((1366, 768))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.tombol_mulai = tk.Button(
            self.root, text="START", font=("system", 16, "bold"), width=20, height=2,
            bg="#b1daf5", fg="black", command=self.tampilkan_pesan
        )
        self.tombol_mulai.place(relx=0.5, rely=0.66, anchor="center")

        self.tombol_klasmen = tk.Button(
            self.root, text="STANDINGS", font=("system", 16, "bold"), width=20, height=2,
            bg="#fdc4c4", fg="black", command=self.buka_standings
        )
        self.tombol_klasmen.place(relx=0.5, rely=0.76, anchor="center")

        self.tombol_info = tk.Button(
            self.root, text="INFO", font=("system", 16, "bold"), width=20, height=2,
            bg="#c297ca", fg="black", command=self.buka_info
        )
        self.tombol_info.place(relx=0.5, rely=0.86, anchor="center")

    def buka_info(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        AppInfo(self.root, self.db)

    def tampilkan_pesan(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        perhitungan.KarateScoringApp(self.root, self.db)

    def buka_standings(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        KarateScoreApp(self.root, self.db)

#kelas untuk nampilin info app 
class AppInfo:
    def __init__(self, root, db):
        self.root = root
        self.db = db

        self.bg_image = Image.open("info.jpg").resize((1366, 768))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        teks = (
            "Aplikasi ini digunakan untuk membantu proses penilaian \n pertandingan Kumite dalam kejuaraan Karate. Sistem menggunakan \n metode bendera (flag system) dan dilengkapi stopwatch, jumlah \n juri serta fitur perhitungan otomatif poin Aka dan Ao.")

        self.canvas.create_text(683, 315, text=teks, font=("system", 17), fill="black", justify="center")

        teks2 = (
            "Nama Aplikasi : Match Day App \nVersi Aplikasi : V0.0 \nDikembangkan Oleh : Kelompok 11 \nFitur Utama : stopwatch, input peserta, dan kontrol nilai.")

        self.canvas.create_text(550, 500, text=teks2, font=("system", 17), fill="black", justify="left")

        self.tombol_home = tk.Button(
            self.root, text="<< HOME", font=("system", 16, "bold"), width=12, height=2,
            bg="#b1daf5", fg="black", command=self.buka_menu
        )
        self.tombol_home.place(relx=0.03, rely=0.92, anchor='w')

        self.tombol_next = tk.Button(
            self.root, text="NEXT >>", font=("system", 16, "bold"), width=12, height=2,
            bg="#fccfcf", fg="black", command=self.buka_TeamPage
        )
        self.tombol_next.place(relx=0.97, rely=0.92, anchor='e')

    def buka_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Menu(self.root, self.db)
        
    def buka_TeamPage(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        TeamPage(self.root, self.db)

#kelas untuk nampilin perkenalan anggota kelompok
class TeamPage:
    def __init__(self, root, db):
        self.root = root
        self.db = db

        self.bg_image = Image.open("AbUs.jpg").resize((1366, 768))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        anggota = [
            {"foto": "zahra.jpg", "nama": "Zahra Ayu Azizah", "npm": "2417051007"},
            {"foto": "indri.jpg", "nama": "Indriyani Talitha Putri", "npm": "2417051013"},
            {"foto": "khaila.jpg", "nama": "Khaila Noverisya Nurdi", "npm": "2417051022"},
            {"foto": "achira.jpg", "nama": "Achira Desya Lucy", "npm": "2417051069"}
        ]

        img_width = 180
        spacing = 60
        total_width = len(anggota) * img_width + (len(anggota) - 1) * spacing
        start_x = (1366 - total_width) // 2
        y_pos = 300

        for i, data in enumerate(anggota):
            img = Image.open(data["foto"]).resize((img_width, img_width))
            photo = ImageTk.PhotoImage(img)
            label_img = tk.Label(self.root, image=photo, bd=0)
            label_img.image = photo
            x_pos = start_x + i * (img_width + spacing)
            label_img.place(x=x_pos, y=y_pos)

            self.canvas.create_text(
                x_pos + img_width // 2, y_pos + img_width + 20,
                text=data["nama"], font=("system", 12, "bold"), fill="black"
            )

            self.canvas.create_text(
                x_pos + img_width // 2, y_pos + img_width + 40,
                text=data["npm"], font=("system", 11), fill="black"
            )

        self.btn_kembali = tk.Button(
            self.root, text="<< BACK", font=("system", 16, "bold"), width=12, height=2,
            bg="#b1daf5", fg="black", command=self.kembali_info
        )
        self.btn_kembali.place(relx=0.03, rely=0.95, anchor="sw")

    def kembali_info(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        AppInfo(self.root, self.db)

#kelas untuk nyambungin dari file perhitungan.py ke main.py
class KarateScoreApp:
    def __init__(self, root, db):
        self.db = db
        self.root = root

        self.bg_image = Image.open("standings.jpg").resize((1366, 768))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.main_frame = tk.Frame(self.canvas, bg="dark blue", bd=0)
        self.canvas.create_window(683, 400, window=self.main_frame)

        font_label = ("System", 17)

        # Label judul riwayat pertandingan
        tk.Label(
            self.main_frame,
            text="ᰔ ⊹˚₊ Riwayat Pertandingan ₊˚⊹ ᰔ",
            font=font_label,
            bg="dark blue",
            fg="white"
        ).grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # Tabel CSV
        self.tree_csv = ttk.Treeview(
            self.main_frame,
            columns=("AO ", "AO Score ", "AKA ", "AKA Score ", "Durasi ", "Divisi"),
            show="headings",
            height=12
        )
        for col, name in zip(
            ("AO ", "AO Score ", "AKA ", "AKA Score ", "Durasi ", "Divisi"),
            ["Nama AO ", "Skor AO ", "Nama AKA ", "Skor AKA ", "Durasi ", "Divisi"]
        ):
            self.tree_csv.heading(col, text=name)
            self.tree_csv.column(col, anchor="center", width=120)
        self.tree_csv.grid(row=1, column=0, columnspan=2, pady=5)

        self.baca_csv()

        self.btn_kembali = tk.Button(
            self.root, text="<< BACK", font=("system", 16, "bold"), width=12, height=2,
            bg="#b1daf5", fg="black", command=self.kembali_menu
        )
        self.btn_kembali.place(relx=0.03, rely=0.92, anchor="w")

        self.tombol_reset = tk.Button(
            self.root, text="RESET", font=("system", 16, "bold"), width=12, height=2,
            bg="#fccfcf", fg="black", command=self.reset_skor
        )
        self.tombol_reset.place(relx=0.95, rely=0.92, anchor="e")

    def kembali_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Menu(self.root, self.db)

    def update_tabel(self):
        for row in self.tree_csv.get_children():
            self.tree_csv.delete(row)

        data = self.db.get_sorted_scores()
        for idx, item in enumerate(data, start=1):
            self.tree_csv.insert("", "end", values=(item["nama"], item["skor"], "", "", "", item["division"]))

    def baca_csv(self):
        try:
            with open("hasil_pertandingan.csv", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header

                data = []
                for row in reader:
                    if len(row) >= 7:
                        try:
                            total = int(row[2]) + int(row[5])
                        except:
                            total = 0
                        data.append((total, row))

                for i in range(len(data)):
                    for j in range(len(data) - i - 1):
                        if data[j][0] < data[j + 1][0]:
                            data[j], data[j + 1] = data[j + 1], data[j]

                for _, row in data:
                    self.tree_csv.insert("", "end", values=(row[1], row[2], row[4], row[5], row[6], row[7]))

        except FileNotFoundError:
            pass

    def hapus_csv():
        with open("hasil_pertandingan.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["AO ", "Nama AO ", "Skor AO ", "AKA ", "Nama AKA ", "Skor AKA ", "Durasi ", "Division"])

    def reset_skor(self):
        # Hapus semua isi tabel tampilan
        for row in self.tree_csv.get_children():
            self.tree_csv.delete(row)

        # Kosongkan file CSV
        with open("hasil_pertandingan.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["AO ", "Nama AO ", "Skor AO ", "AKA ", "Nama AKA ", "Skor AKA ", "Durasi ", "Division"])

        # Kosongkan memori
        self.db.reset()

#untuk memanggil fungsi yang ingin ditampilin
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Match Day App")
    root.geometry("1366x768")
    root.resizable(True, True)
    db = ScoreDatabase()
    app = LoadingPage(root, db)
    root.mainloop()
