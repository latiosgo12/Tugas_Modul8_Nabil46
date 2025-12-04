import tkinter as tk
from tkinter import messagebox, ttk

# =============== CLASS Buku (OOP + Enkapsulasi) ===============
class Buku:
    def __init__(self, judul, status):
        self.__judul = judul  # private attribute
        self.__status = status

    def get_judul(self):
        return self.__judul

    def get_status(self):
        return self.__status

    def set_status(self, status_baru):
        self.__status = status_baru


# =============== Data Buku ===============
daftar_buku = []


# =============== Fungsi GUI ===============
def tambah_buku():
    judul = entry_judul.get()
    status = combo_status.get()

    if judul == "" or status == "":
        messagebox.showwarning("Peringatan", "Data tidak boleh kosong!")
        return

    buku_baru = Buku(judul, status)
    daftar_buku.append(buku_baru)

    messagebox.showinfo("Berhasil", f"Buku '{judul}' berhasil ditambahkan!")
    entry_judul.delete(0, tk.END)
    tampilkan_daftar()


def tampilkan_daftar():
    list_buku.delete(*list_buku.get_children())
    for buku in daftar_buku:
        status = buku.get_status()
        
        # If Else menentukan warna status
        if status == "Tersedia":
            warna = "green"
        else:
            warna = "red"

        list_buku.insert("", tk.END, values=(buku.get_judul(), status), tags=(warna,))
        list_buku.tag_configure("green", foreground="green")
        list_buku.tag_configure("red", foreground="red")


# =============== GUI Setup ===============
root = tk.Tk()
root.title("Manajemen Buku Perpustakaan")
root.geometry("420x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Judul Buku:").grid(row=0, column=0, sticky="w")
entry_judul = tk.Entry(frame, width=30)
entry_judul.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Status Buku:").grid(row=1, column=0, sticky="w")
combo_status = ttk.Combobox(frame, values=["Tersedia", "Dipinjam"], width=27)
combo_status.grid(row=1, column=1, pady=5)

btn_tambah = tk.Button(frame, text="Tambah Buku", command=tambah_buku)
btn_tambah.grid(row=2, columnspan=2, pady=10)

# Table List
list_buku = ttk.Treeview(root, columns=("judul", "status"), show="headings", height=10)
list_buku.heading("judul", text="Judul Buku")
list_buku.heading("status", text="Status")
list_buku.pack()

root.mainloop()
