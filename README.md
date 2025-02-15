# Capstone_Modul1
## Kirana Azhura

 # Program Klinik Hewan
## Tentang Program
Program Klinik Hewan ini dirancang untuk membantu admin dalam mengelola data pasien hewan, termasuk menambah pasien baru, pembaruan data (status, layanan, tanggal keluar), menghapus data, serta melihat riwayat pasien yang dihapus. Admin dapat dengan mudah menambah, menghapus, memperbarui, dan melihat data pasien dengan sistem berbasis Python.
________________________________________
## Fitur Utama
✅ Navigasi Menu Sistem menu interaktif untuk memilih fitur yang diinginkan.

✅ Tampilkan Daftar Pasien – Admin dapat melihat daftar pasien, baik secara keseluruhan maupun dengan menginput kode pasien yang ingin dilihat datanya.✅ Tambah Pasien Baru – Admin dapat mendaftarkan pasien baru.

✅ Hapus Pasien – Admin dapat menghapus data pasien yang sudah tidak aktif.

✅ Update Data Pasien – Admin bisa mengubah informasi layanan, status, atau tanggal keluar pasien berdasarkan kode unik.

✅ Riwayat Pasien – Admin dapat melihat Riwayat pasien yang sudah dihapus.

________________________________________
## CRUD Function
1.	Create (Menambahkan data)
  •	Menambahkan pasien hewan baru ke dalam `tambah()`
  •	Admin dapat menambahkan hewan baru ke daftar pasien dengan menginput kode, tanggal_masuk, nama pemilik, nama hewan, jenis hewan, pelayanan yang diinginkan, status, serta tanggal keluar hewan.
2.	Read (Membaca Data)
  •	Menampilkan daftar pasien baik secara keseluruhan maupun dengan menginput kode pasien yang ingin dilihat datanya:  `menu_daftar()`
  •	Menampilkan Riwayat pasien yang sudah dihapus `Riwayat()`
3.	Update (Mengubah atau Memperbarui data)
  •	Mengubah layanan atau status jika dibutuhkan, serta mengubah tanggal keluar pasien dari yang sebelumnya masin proses menjadi tanggal keluarnya: `ubah()`
4.	Delete (Menghapus Data)
  •	Menghapus data pasien jika sudah tidak aktif `hapus()`
________________________________________
## Cara Menggunakan
1.	Jalankan program menggunakan Python.
2.	Masukkan `password` admin: `81101`
3.	Pilih menu yang diinginkan dari daftar yang tersedia.
4.	Ikuti petunjuk untuk menambah, memperbarui, atau menghapus data.
5.	Keluar dari program dengan memilih opsi yang disediakan.
________________________________________
## Struktur Data
Program ini menyimpan data pasien dalam bentuk dictionary:

daftar_pasien = {

    'kode' : ['C11', 'D11', 'C12'],
    'tanggal_masuk': [datetime.date(2025, 1, 2).strftime('%Y-%m-%d'),
                    datetime.date(2025, 1, 15).strftime('%Y-%m-%d'),
                    datetime.date(2025, 2, 10).strftime('%Y-%m-%d')],
    'nama_pemilik' : ['Rey', 'Agus', 'Cantika'],
    'nama_hewan' : ['Boby', 'Doggy', 'Mochi'],
    'jenis' : ['Kucing', 'Anjing', 'Kucing'],
    'pelayanan' : ['Suntik Kutu', 'Patah Kaki', 'Grooming'],
    'status' : ['selesai', 'rawat inap', 'selesai'],
    'tanggal_keluar': [datetime.date(2025, 1, 2).strftime('%Y-%m-%d'),
                    'belum keluar',
                    datetime.date(2025, 2, 10).strftime('%Y-%m-%d')]
      }
      
Setiap pasien memiliki kode unik yang digunakan untuk identifikasi dalam sistem.

________________________________________
## Validasi Input
🔹 Admin harus memasukkan kode pasien yang valid saat memperbarui atau menghapus data.

🔹 Jika input tidak sesuai, program akan meminta admin mengulanginya hingga benar.

🔹 Hanya angka yang diterima untuk pilihan menu.
________________________________________
## Pustaka yang digunakan:
•	`tabulate` : Pustaka ini digunakan untuk menampilkan data pasien hewan dalam format tabel yang rapi di terminal.

•	`datetime` : Pustaka ini digunakan untuk menanganai tanggal dan waktu, memungkinkan sistem untuk mengelola tanggal masuk dan tanggal keluar secara efektif

•	`os`       : Pustaka ini digunakan untuk menghapus tampilan terminal yang sudah tidak dibutuhkan, sehingga tampilan terminal akan lebih bersih.
________________________________________
## Catatan
🔸 Program ini belum menggunakan database, sehingga data hanya tersimpan sementara saat program berjalan.

🔸 Pastikan Python sudah terinstal sebelum menjalankan program.

🔸 Install pustaka tabulate jika belum tersedia dengan menjalankan perintah berikut: pip install tabulate

________________________________________
Admin Klinik Hewan - Program ini dibuat untuk mempermudah administrasi klinik hewan dalam pencatatan pasien. 
