import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import requests
from urllib.parse import urlparse
import pathlib

# Konfigurasi kredensial Cloudinary
cloudinary.config(
    cloud_name="dl2ijoilh",  # Ganti dengan cloud_name Anda
    api_key="728318425888881",  # Ganti dengan api_key Anda
    api_secret="ae-qYFtVNSnChVkT-Y1YXkb-jD8"  # Ganti dengan api_secret Anda
)

# Fungsi untuk mengunggah file ke Cloudinary
def upload_to_cloudinary(input_file_path):
    try:
        # Mengunggah file gambar ke Cloudinary
        response = cloudinary.uploader.upload(input_file_path)
        print(f"Berhasil mengunggah {input_file_path} ke Cloudinary.")
        return response
    except Exception as e:
        print(f"Gagal mengunggah {input_file_path} ke Cloudinary: {e}")
        return None

# Fungsi untuk mengunduh file dari URL
def download_file(url, output_path):
    try:
        # Mengunduh file dari URL
        response = requests.get(url)
        with open(output_path, "wb") as file:
            file.write(response.content)
        print(f"Berhasil mengunduh file ke {output_path}")
    except Exception as e:
        print(f"Gagal mengunduh file: {e}")

# Fungsi untuk mengonversi gambar menggunakan Cloudinary dan mengunduhnya
def convert_and_download(input_file_path, output_folder, output_format):
    # Unggah file ke Cloudinary
    upload_response = upload_to_cloudinary(input_file_path)

    if upload_response:
        # Mendapatkan URL file yang sudah diunggah
        cloudinary_url = upload_response['url']

        # Membuat URL dengan transformasi untuk mengonversi gambar ke format yang dipilih
        converted_url = f"{cloudinary_url}?f_auto&format={output_format}"

        # Tentukan nama file output
        output_filename = os.path.splitext(os.path.basename(input_file_path))[0] + f".{output_format}"
        output_path = os.path.join(output_folder, output_filename)

        # Download file dari Cloudinary
        download_file(converted_url, output_path)

# Fungsi untuk memilih file gambar menggunakan file dialog
def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.heic")])
    if file_path:
        input_file_label.config(text=f"File input: {file_path}")
        return file_path
    else:
        return None

# Fungsi untuk memilih folder gambar menggunakan file dialog
def select_input_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_file_label.config(text=f"Folder input: {folder_path}")
        return folder_path
    else:
        return None

# Fungsi untuk memilih folder output menggunakan file dialog
def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_label.config(text=f"Folder output: {folder_path}")
        return folder_path
    else:
        return None

# Fungsi untuk menangani tombol konversi
def convert_image():
    input_file_or_folder_path = input_file_label.cget("text").replace("File input: ", "").replace("Folder input: ", "")
    output_folder_path = output_folder_label.cget("text").replace("Folder output: ", "")
    output_format = format_var.get()

    if not input_file_or_folder_path or not output_folder_path:
        messagebox.showerror("Error", "Pilih file atau folder dan folder output terlebih dahulu!")
        return
    
    if os.path.isdir(input_file_or_folder_path):
        # Jika folder, proses semua file gambar dalam folder
        for filename in os.listdir(input_file_or_folder_path):
            file_path = os.path.join(input_file_or_folder_path, filename)
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".heic")):
                try:
                    convert_and_download(file_path, output_folder_path, output_format)
                except Exception as e:
                    print(f"Gagal mengonversi {filename}: {e}")
        messagebox.showinfo("Sukses", f"Konversi berhasil! Semua gambar disimpan di {output_folder_path}")
    else:
        # Jika file, hanya satu file yang akan diproses
        try:
            convert_and_download(input_file_or_folder_path, output_folder_path, output_format)
            messagebox.showinfo("Sukses", f"Konversi berhasil! Gambar disimpan di {output_folder_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengonversi gambar: {e}")

# GUI Tkinter
root = tk.Tk()
root.title("Konvert gambar")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# Mengatur font dan warna untuk tampilan lebih baik
font = ("Arial", 12)
highlight_font = ("Arial", 14, "bold")
bg_color = "#f0f0f0"
fg_color = "#333333"
button_color = "#4CAF50"
button_hover_color = "#45a049"

# Fungsi untuk memberi efek shadow
def add_shadow(widget, bg_color="#e0e0e0", fg_color="#333"):
    widget.config(bg=bg_color, fg=fg_color, bd=2, relief="solid", highlightthickness=2, highlightbackground="#ccc")

# Label untuk menampilkan file input
input_file_label = tk.Label(root, text="Pilih file atau folder gambar untuk dikonversi", width=60, height=2, anchor="w", font=font)
input_file_label.pack(pady=10, anchor="w", padx=20)
add_shadow(input_file_label)

# Tombol untuk memilih file input
select_input_file_button = tk.Button(root, text="Pilih File", command=select_input_file, width=18, height=2, font=highlight_font, bg=button_color, fg="white")
select_input_file_button.pack(pady=5)
add_shadow(select_input_file_button)

# Tombol untuk memilih folder input
select_input_folder_button = tk.Button(root, text="Pilih Folder", command=select_input_folder, width=18, height=2, font=highlight_font, bg=button_color, fg="white")
select_input_folder_button.pack(pady=5)
add_shadow(select_input_folder_button)

# Label untuk menampilkan folder output
output_folder_label = tk.Label(root, text="Pilih folder untuk menyimpan gambar", width=60, height=2, anchor="w", font=font)
output_folder_label.pack(pady=10, anchor="w", padx=20)
add_shadow(output_folder_label)

# Tombol untuk memilih folder output
select_output_button = tk.Button(root, text="Pilih Folder", command=select_output_folder, width=18, height=2, font=highlight_font, bg=button_color, fg="white")
select_output_button.pack(pady=5)
add_shadow(select_output_button)

# Pilihan format output
format_label = tk.Label(root, text="Pilih format output", width=60, height=2, anchor="w", font=font)
format_label.pack(pady=10, anchor="w", padx=20)
add_shadow(format_label)

format_var = tk.StringVar()
format_var.set("png")  # Default format

format_option_menu = tk.OptionMenu(root, format_var, "png", "jpg", "jpeg", "bmp", "gif")
format_option_menu.config(width=18, height=2, font=highlight_font, bg=button_color, fg="white")
format_option_menu.pack(pady=5)
add_shadow(format_option_menu)

# Tombol konversi
convert_button = tk.Button(root, text="Konversi", command=convert_image, width=18, height=2, font=highlight_font, bg=button_color, fg="white")
convert_button.pack(pady=20)
add_shadow(convert_button)

# Run the Tkinter event loop
root.mainloop()
