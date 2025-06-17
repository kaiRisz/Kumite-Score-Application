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
