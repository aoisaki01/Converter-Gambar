Gambar Konversi dengan Cloudinary
Aplikasi ini buat konversi gambar pake Cloudinary. Lo bisa pilih gambar atau folder, terus convert ke format apapun yang lo mau. Gambar yang udah di-convert langsung ke-download deh.

Fitur
Pilih gambar atau folder buat di-convert.
Pilih format output (PNG, JPG, JPEG, BMP, GIF).
Bisa batch konversi kalo pilih folder.
Pake Cloudinary buat konversi otomatis.
Gambar yang udah di-convert bakal ke-download ke folder yang lo pilih.
Persyaratan
Sebelum jalanin aplikasi ini, lo harus install beberapa dependencies:

Python 3.x (udah pasti)
Pillow (PIL) – Buat buka dan olah gambar.
Cloudinary Python SDK – Buat connect ke API Cloudinary.
Requests – Buat download gambar dari URL.
Tkinter – Buat GUI aplikasi.
Cara Install
Clone Repo:

Lo bisa clone repo ini pake:
bash
Copy
Edit
git clone https://github.com/username/repository-name.git
Install Dependensi:

Install semua dependensi pake:
bash
Copy
Edit
pip install -r requirements.txt
Atau install manual:

bash
Copy
Edit
pip install pillow cloudinary requests
Setup Cloudinary:

Lo harus daftar akun di Cloudinary buat dapetin cloud_name, api_key, dan api_secret.
Masukin kredensial lo di kode (app.py).
Penggunaan
Jalankan Aplikasi
Setelah semua install, tinggal jalankan pake:

bash
Copy
Edit
python app.py
GUI bakal muncul, dan lo bisa mulai konversi gambar.

Langkah-Langkah:
Pilih Gambar:

Klik Pilih File buat pilih satu gambar buat di-convert.
Pilih Folder:

Klik Pilih Folder kalo lo mau batch convert gambar di dalam folder.
Pilih Folder Output:

Klik Pilih Folder buat tentuin tempat nyimpen gambar yang udah di-convert.
Pilih Format Output:

Pilih format gambar yang lo mau: PNG, JPG, JPEG, BMP, atau GIF.
Konversi:

Klik Konversi buat mulai proses. Gambar yang udah di-convert bakal otomatis ke-download.
Format yang Didukung
PNG
JPG
JPEG
BMP
GIF
Cloudinary API
Pake Cloudinary buat convert gambar. Lo cukup upload gambar ke Cloudinary, terus gambar yang udah di-convert bakal diunduh balik lewat URL.

Kredensial Cloudinary
Di app.py, jangan lupa ganti kredensial Cloudinary lo:

python
Copy
Edit
cloudinary.config(
    cloud_name="YOUR_CLOUD_NAME", 
    api_key="YOUR_API_KEY", 
    api_secret="YOUR_API_SECRET"
)
Troubleshooting
Error "cannot identify image file":

Pastikan gambar lo formatnya bener dan didukung aplikasi.
Kalo lo upload HEIC, coba convert dulu ke format lain.
Cloudinary ga bisa upload:

Cek kredensial Cloudinary lo, pastiin bener.
Pastikan koneksi internet lo lancar.
Tampilan berantakan:

Pastikan Python dan Tkinter lo compatible.
Kontribusi
Lo bisa kontribusi kalo mau, tinggal pull request aja. Jangan lupa jelasin perubahan lo ya!

Lisensi
Aplikasi ini dilisensikan di bawah MIT License.

Di sini, gue singkatin aja dan bikin lebih casual. Lo bisa tinggalin komentar atau pull request kalau ada yang perlu diperbaiki!
