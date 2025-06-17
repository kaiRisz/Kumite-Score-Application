import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import csv
from main import Menu

#untuk membuat bagan perhitungan skor
class KarateScoringApp:
    def __init__(self, root, db):  
        self.root = root
        self.db = db
        self.root.title("Karate Scoring System")
        self.root.geometry("1366x768")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.running2 = False
        self.start_time2 = 0
        self.elapsed_time2 = 0
        self.stopwatch_visible = True

        red_flag_image = Image.open("red_flag.png").resize((250, 250), Image.Resampling.LANCZOS)
        self.red_flag_photo = ImageTk.PhotoImage(red_flag_image)
        blue_flag_image = Image.open("blue_flag.png").resize((250, 250), Image.Resampling.LANCZOS)
        self.blue_flag_photo = ImageTk.PhotoImage(blue_flag_image)

        self.ao_score = 0
        self.aka_score = 0

        self.canvas = tk.Canvas(root, width=1366, height=768)
        self.canvas.pack(fill="both", expand=True)

        self.ao_frame = tk.Frame(self.canvas, bg="blue", width=683, height=768)
        self.ao_frame.place(x=0, y=0)
        self.aka_frame = tk.Frame(self.canvas, bg="red", width=683, height=768)
        self.aka_frame.place(x=683, y=0)

        #ini bagian buat header
        self.header_frame = tk.Frame(self.canvas, bg="black", height=60, width=1366)
        self.header_frame.place(x=0, y=0)

        self.ao_name_entry = tk.Entry(self.header_frame, font=("Helvetica", 14), width=20)
        self.ao_name_entry.place(x=20, y=20)
        tk.Label(self.header_frame, text="Write Ao name", font=("Helvetica", 10), bg="black", fg="white").place(x=20, y=2)

        tk.Label(self.header_frame, text="Division:", font=("Helvetica", 14), bg="black", fg="white").place(x=620, y=5)
        self.division_entry = tk.Entry(self.header_frame, font=("Helvetica", 14), width=15)
        self.division_entry.place(x=720, y=12)

        self.aka_name_entry = tk.Entry(self.header_frame, font=("Helvetica", 14), width=20)
        self.aka_name_entry.place(x=1120, y=20)
        tk.Label(self.header_frame, text="Write Aka name", font=("Helvetica", 10), bg="black", fg="white").place(x=1120, y=2)

        tk.Label(self.canvas, text="Judges", font=("Helvetica", 14), bg="green", fg="white").place(x=650, y=70)
        self.judges_spinbox = tk.Spinbox(self.canvas, from_=1, to=9, font=("Helvetica", 14), width=5)
        self.judges_spinbox.place(x=648, y=100)

        #UI buat referee (wasit yang ngasih score berdasarkan penilaian judges)
        self.ao_score_label = tk.Label(self.ao_frame, text="0", font=("Helvetica", 200), bg="blue", fg="white")
        self.ao_score_label.place(x=100, y=100)
        tk.Button(self.ao_frame, text="+1", font=("Helvetica", 18), command=self.ao_add).place(x=110, y=410)
        tk.Button(self.ao_frame, text="-1", font=("Helvetica", 18), command=self.ao_sub).place(x=220, y=410)
        self.ao_flag_frame = tk.Frame(self.ao_frame, width=250, height=250, bg="white")
        self.ao_flag_frame.place(x=390, y=190)
        self.ao_flag_label = tk.Label(self.ao_flag_frame, image=self.blue_flag_photo, bg="white")
        self.ao_flag_label.pack()

        self.aka_score_label = tk.Label(self.aka_frame, text="0", font=("Helvetica", 200), bg="red", fg="white")
        self.aka_score_label.place(x=100, y=100)
        tk.Button(self.aka_frame, text="+1", font=("Helvetica", 18), command=self.aka_add).place(x=110, y=410)
        tk.Button(self.aka_frame, text="-1", font=("Helvetica", 18), command=self.aka_sub).place(x=220, y=410)
        self.aka_flag_frame = tk.Frame(self.aka_frame, width=250, height=250, bg="white")
        self.aka_flag_frame.place(x=390, y=190)
        self.aka_flag_label = tk.Label(self.aka_flag_frame, image=self.red_flag_photo, bg="white")
        self.aka_flag_label.pack()

        #UI stopwatch
        self.stopwatch_label = tk.Label(self.canvas, text="0:00", font=("Helvetica", 85), bg="dark blue", fg="white")
        self.stopwatch_label.place(x=418, y=480)
        self.stopwatch2_label = tk.Label(self.canvas, text="0:00", font=("Helvetica", 85), bg="dark red", fg="white")
        self.stopwatch2_label.place(x=1104, y=480)
        self.start_btn = tk.Button(self.canvas, text="Start", font=("Helvetica", 20), bg="green", fg="white", command=self.toggle_timer)
        self.start_btn.place(x=200, y=510)

        # Footer
        self.control_frame = tk.Frame(self.canvas, bg="black")
        self.control_frame.place(x=0, y=637, width=1366, height=60)

        self.show_hide_btn = tk.Button(self.control_frame, text="Show/Hide Stopwatch", font=("Helvetica", 12), bg="green", fg="white", command=self.toggle_stopwatch)
        self.show_hide_btn.place(x=10, y=10)

        self.ao_shikkaku_btn = tk.Button(self.control_frame, text="Shikkaku", font=("Helvetica", 12), bg="dark blue", fg="white", command=self.ao_shikkaku)
        self.ao_shikkaku_btn.place(x=300, y=10)

        self.ao_kikken_btn = tk.Button(self.control_frame, text="Kikken", font=("Helvetica", 12), bg="dark blue", fg="white", command=self.ao_kikken)
        self.ao_kikken_btn.place(x=500, y=10)

        self.done_btn = tk.Button(self.control_frame, text="Done", font=("Helvetica", 12), bg="lightgreen", command=self.done)
        self.done_btn.place(x=660, y=10)

        self.aka_shikkaku_btn = tk.Button(self.control_frame, text="Shikkaku", font=("Helvetica", 12), bg="dark red", fg="white", command=self.aka_shikkaku)
        self.aka_shikkaku_btn.place(x=800, y=10)

        self.aka_kikken_btn = tk.Button(self.control_frame, text="Kikken", font=("Helvetica", 12), bg="dark red", fg="white", command=self.aka_kikken)
        self.aka_kikken_btn.place(x=1000, y=10)

        self.reset_btn = tk.Button(self.control_frame, text="Reset", font=("Helvetica", 12), bg="red", fg="white", command=self.reset)
        self.reset_btn.place(x=1180, y=10)

        self.back_btn = tk.Button(self.control_frame, text="Back", font=("Helvetica", 12), bg="light blue", fg="black", command=self.go_back)
        self.back_btn.place(x=1275, y=10)

        #yang ini biar pas direset, waktunya ngulang dari awal lagi
        self.update_timer()

    #method buat nambahin score +1 ke ao
    def ao_add(self):
        self.ao_score += 1
        self.ao_score_label.config(text=str(self.ao_score), font=("Helvetica", 200))

    #method buat ngurangin score -1 ke ao
    def ao_sub(self):
        self.ao_score = max(0, self.ao_score - 1)
        self.ao_score_label.config(text=str(self.ao_score), font=("Helvetica", 200))

    #method buat nambahin score +1 ke aka
    def aka_add(self):
        self.aka_score += 1
        self.aka_score_label.config(text=str(self.aka_score), font=("Helvetica", 200))

    #method buat ngurangin score -1 ke aka
    def aka_sub(self):
        self.aka_score = max(0, self.aka_score - 1)
        self.aka_score_label.config(text=str(self.aka_score), font=("Helvetica", 200))
        
    #method biar pas button back dipencet tampilan score balik ke menu awal
    def go_back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        Menu(self.root, self.db)

    #method buat ngatur timernya
    def toggle_timer(self):
        if not self.running and not self.running2: #ini start
            self.start_time = time.time() - self.elapsed_time
            self.start_time2 = time.time() - self.elapsed_time2
            self.running = True
            self.running2 = True
            self.start_btn.config(text="Pause")
        else: #ini pause
            self.elapsed_time = time.time() - self.start_time
            self.elapsed_time2 = time.time() - self.start_time2
            self.running = False
            self.running2 = False
            self.start_btn.config(text="Start")
    
    #method untuk ngatur waktu juga enih pas udh 3 menit yea kak
    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            if self.elapsed_time >= 180:
                self.running = False
                self.running2 = False
                self.start_btn.config(text="Start")
                messagebox.showinfo("Time's up", "3 minutes have passed. Time is up!")
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            self.stopwatch_label.config(text=f"{minutes}:{seconds:02}")
        if self.running2:
            self.elapsed_time2 = time.time() - self.start_time2
            minutes2 = int(self.elapsed_time2 // 60)
            seconds2 = int(self.elapsed_time2 % 60)
            self.stopwatch2_label.config(text=f"{minutes2}:{seconds2:02}")
        self.root.after(1000, self.update_timer)

    #untuk munculin sama ilangin UI stopwatchnyaaa
    def toggle_stopwatch(self):
        if self.stopwatch_visible:
            self.stopwatch_label.place_forget()
            self.stopwatch2_label.place_forget()
        else:
            self.stopwatch_label.place(x=418, y=480)
            self.stopwatch2_label.place(x=1104, y=480)
        self.stopwatch_visible = not self.stopwatch_visible

    #method biar pas tombol shikakku dipencet keluar tulisan "Penalty!" di ao
    def ao_shikkaku(self):
        self.ao_score_label.config(text="Penalty!", font=("Helvetica", 50))

    #method biar pas tombol kikken dipencet keluar tulisan "Disqualified!" di ao
    def ao_kikken(self):
        self.ao_score_label.config(text="Disqualified!", font=("Helvetica", 50))

    #method biar pas tombol shikakku dipencet keluar tulisan "Penalty!" di aka
    def aka_shikkaku(self):
        self.aka_score_label.config(text="Penalty!", font=("Helvetica", 50))

     #method biar pas tombol kikken dipencet keluar tulisan "Disqualified!" di aka
    def aka_kikken(self):
        self.aka_score_label.config(text="Disqualified!", font=("Helvetica", 50))

    #method buat nampilin skor yang udah didapatkan ke message box
    def done(self):
        self.running = False
        self.running2 = False
        self.start_btn.config(text="Start")

        ao_name = self.ao_name_entry.get()
        aka_name = self.aka_name_entry.get()
        division = self.division_entry.get()
        judges = self.judges_spinbox.get()
        ao_score = self.ao_score
        aka_score = self.aka_score

        # Hitung durasi stopwatch
        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        durasi_waktu = f"{minutes}:{seconds:02}"

        result = f"{ao_name} (Ao): {ao_score}\n{aka_name} (Aka): {aka_score}\nJudges: {judges}"
        messagebox.showinfo("Match Result", result)

        # Simpan ke CSV + database
        self.simpan_hasil(durasi_waktu)

    #method buat ngambil dan nyimpen skor yang udah didapatkan ke csv
    def simpan_hasil(self, durasi_waktu):
        ao_name = self.ao_name_entry.get()
        aka_name = self.aka_name_entry.get()
        division = self.division_entry.get()
        ao_score = self.ao_score
        aka_score = self.aka_score

        with open("hasil_pertandingan.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["AO", ao_name, ao_score,"AKA", aka_name, aka_score, durasi_waktu, division])

        # nyimpen ke database file csvnya
        self.db.tambah_skor(ao_name, ao_score, division)
        self.db.tambah_skor(aka_name, aka_score, division)


    #buat ngembaliin semua tampilan yang udah di jalanin ke setelan awal
    def reset(self):
        self.ao_score = 0
        self.aka_score = 0
        self.elapsed_time = 0
        self.elapsed_time2 = 0
        self.running = False
        self.running2 = False
        self.start_btn.config(text="Start")
        self.stopwatch_label.config(text="0:00", font=("Helvetica", 85))
        self.stopwatch2_label.config(text="0:00", font=("Helvetica", 85))
        self.ao_score_label.config(text="0", font=("Helvetica", 200))
        self.aka_score_label.config(text="0", font=("Helvetica", 200))
        self.ao_name_entry.delete(0, tk.END)
        self.aka_name_entry.delete(0, tk.END)
        self.division_entry.delete(0, tk.END)

#buat munculin jendela baru yang isinya aplikasi scoring karate, terus dia pake data dari db buat nyimpen atau nampilin skor.
def run_scoring_app(db):
    root = tk.Toplevel()
    app = KarateScoringApp(root, db)
    root.mainloop()
