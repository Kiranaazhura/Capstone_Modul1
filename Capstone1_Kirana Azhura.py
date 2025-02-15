# APP KLINIK HEWAN BAHAGIA
# PSSWORD ADMIN 81101

from tabulate import tabulate
import datetime 
import os
import platform
def clear_terminal(): # agar terminal bersih saat run
    system = platform.system().lower()
    if system == 'windows':
        os.system('cls')
    else:
        os.system('clear')


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
headers1 = ['Kode', 'Tanggal_Masuk', 'Nama Pemilik', 'Nama_Hewan', 'Jenis Hewan', 'Pelayanan','Status', 'Tanggal_Keluar' ]

rwy = [] # keranjang kosong untuk menu riwayat

def tabel_daftarHewan():
    print('\nDaftar Pasien Klinik Hewan Bahagia')
    print(tabulate(daftar_pasien, headers=headers1, tablefmt='grid').title())

daftar_kode = []

# menu untuk melihat Daftar Hewan
# menu Read
def menu_daftar():
    clear_terminal()
    while True:
        print("\t\nList Menu: \n"
              "\t1. Menampilkan Daftar Pasien\n"
              "\t2. Menampilkan Pasien Berdasarkan Kode\n"
            "\t3. Kembali ke Menu utama\n")
        try: # agar disaat input menu selain angka yang ada dipilihan/input str program tidak eror
            input_daftar = int(input('Masukkan Menu yang ingin dipilih: '))
        except ValueError:
            print('Inputan tidak valid, silakan masukkan angka (1-3)')
            continue
        print()
        if input_daftar == 1:
            tabel_daftarHewan()

        elif input_daftar == 2 :
            while True:
                input_read = str(input('Masukkan kode pasien yang ingin ditampilkan: ')).upper()
                if input_read in daftar_pasien['kode']:
                    index = daftar_pasien['kode'].index(input_read)
                    daftar_kode.append([daftar_pasien['kode'][index], daftar_pasien['tanggal_masuk'][index], daftar_pasien['nama_pemilik'][index], daftar_pasien['nama_hewan'][index], daftar_pasien['jenis'][index], daftar_pasien['pelayanan'][index], daftar_pasien['status'][index], daftar_pasien['tanggal_keluar'][index]])
                    print(tabulate(daftar_kode, headers=headers1, tablefmt='grid').title())
                    break
                elif input_read not in daftar_pasien['kode']:
                    print('Kode yang dimasukkan tidak tersedia')
                    continue

        elif input_daftar == 3:
            clear_terminal()
            break

# menu untuk menambahkan daftar hewan
# create
def tambah():
    clear_terminal()
    while True:
        print("\t\nList Menu: \n"
              "\t1. Menambahkan Data Pasien\n"
             "\t2. Kembali ke Menu utama\n")
        try:
            input_tambah = int(input('Masukkan Menu yang ingin dipilih: '))
        except ValueError:
            print('Inputan tidak valid, silakan masukkan angka')
            continue
        if input_tambah == 1:
            tabel_daftarHewan()
            while True:
                kode_baru = input(str('Masukkan kode hewan yang akan ditambahkan: ')).strip().upper() # agar inputan tidak bisa spasi saja
                print()
                if kode_baru in daftar_pasien['kode']: # agar kode tidak duplikat
                    print('Kode hewan yang dimasukkan sudah ada ')
                    while True:
                        lanjut_tambah = input('Jadi menambahkan hewan? [Y/N]: ' ).upper()
                        print()
                        if lanjut_tambah == 'Y':
                            break
                        elif lanjut_tambah == 'N':
                            clear_terminal()
                            return
                        else:
                            print('Inputan tidak valid, silakan input Y/N')
                            continue

                elif kode_baru == '': # agar inputan kode tidak boleh kosong 
                    print('Input kode tidak boleh kosong!')
                    print()
                    continue

                else:
                    while True:
                        try:
                            tanggal_m_baru = input('Masukkan tanggal (YYYY-MM-DD): ')
                            tanggal_m_baru = datetime.datetime.strptime(tanggal_m_baru, '%Y-%m-%d').date()
                        except ValueError:
                            print("Format tanggal salah. Pastikan formatnya YYYY-MM-DD.")
                            print()
                            continue
                        break

                    pemilik_baru = input('Masukkan nama pemilik: ')
                    hewan_baru = input('Masukkan nama hewan: ')  
                    jenis_baru = input('Masukkan jenis hewan: ')    
                    pelayanan_baru = input('Masukkan pelayanan yang dibutuhkan: ')
                    status_baru = input('Masukkan status hewan: ') 
                    tanggal_k_baru = input('Masukkan tanggal keluar: ')
                    daftar_pasien['kode'].append(kode_baru)
                    daftar_pasien['tanggal_masuk'].append(tanggal_m_baru.strftime('%Y-%m-%d'))
                    daftar_pasien['nama_pemilik'].append(pemilik_baru)
                    daftar_pasien['nama_hewan'].append(hewan_baru)
                    daftar_pasien['jenis'].append(jenis_baru)
                    daftar_pasien['pelayanan'].append(pelayanan_baru)
                    daftar_pasien['status'].append(status_baru)
                    daftar_pasien['tanggal_keluar'].append(tanggal_k_baru)
                    daftar_pasien
                    clear_terminal()
                    print('Hewan berhasil ditambahkan!')
                    tabel_daftarHewan()

                    while True:
                        tambah_lagi = input('Ingin menambahkan hewan lain? [Y/N]: ' ).upper()
                        if tambah_lagi == 'Y':
                            break
                        elif tambah_lagi == 'N':
                            clear_terminal()
                            return
                        else:
                            print('Inputan tidak valid, silakan input Y/N')
                            print()
                            continue

        if input_tambah == 2:
            clear_terminal()
            break

# menu untuk menghapus daftar hewan 
#delete
def hapus():
    clear_terminal()
    while True:
        print("\t\nList Menu: \n"
              "\t1. Menghapus Data Pasien\n"
             "\t2. Kembali ke Menu utama\n")
        try:
            input_hapus = int(input('Masukkan Menu yang ingin dipilih: '))
        except ValueError:
            print('Inputan tidak valid, silakan masukkan angka')
            print()
            continue
        if input_hapus == 1:
            clear_terminal()
            tabel_daftarHewan()
            while True:
                del_hewan = str(input('Masukkan kode hewan yang ingin dihapus: ')).upper()
                print()
                if del_hewan in daftar_pasien['kode']:
                    index_hapus = daftar_pasien['kode'].index(del_hewan)
                    # untuk memasukkan yang sudah dihapus ke dalam riwayat
                    rwy.append([daftar_pasien['kode'][index_hapus], daftar_pasien['tanggal_masuk'][index_hapus], daftar_pasien['nama_pemilik'][index_hapus], daftar_pasien['nama_hewan'][index_hapus], daftar_pasien['jenis'][index_hapus], daftar_pasien['pelayanan'][index_hapus], daftar_pasien['status'][index_hapus], daftar_pasien['tanggal_keluar'][index_hapus]])
                    
                    del daftar_pasien['kode'][index_hapus]
                    del daftar_pasien['tanggal_masuk'][index_hapus]
                    del daftar_pasien['nama_pemilik'][index_hapus]
                    del daftar_pasien['nama_hewan'][index_hapus]
                    del daftar_pasien['jenis'][index_hapus]
                    del daftar_pasien['pelayanan'][index_hapus]
                    del daftar_pasien['status'][index_hapus]
                    del daftar_pasien['tanggal_keluar'][index_hapus]
                    print('Hewan berhasil dihapus')
                    tabel_daftarHewan()
                   
                    while True:
                        cek_hapus_lain = input('Apakah Anda ingin menghapus data lain? (Y/N): ').upper()
                        print()
                        if cek_hapus_lain == 'Y':
                            break

                        elif cek_hapus_lain == 'N':
                            return

                        else:
                            print('Inputan tidak valid, silakan input Y/N')
                            print()
                            continue

                else:
                    print('Data hewan tidak tersedia')
                    while True:
                        cek_jadi_hapus = input('Apakah Anda jadi menghapus data? (Y/N): ').upper()
                        print()
                        if cek_jadi_hapus == 'Y':
                            break

                        elif cek_jadi_hapus == 'N':
                            return

                        else:
                            print('Inputan tidak valid, silakan input Y/N')
                            print()
                            continue
                continue
        elif input_hapus == 2:
            clear_terminal()
            break

# menu untuk mengubah data hewan
# update
def ubah():
    clear_terminal
    while True:
        print("\t\nList Menu: \n"
              "\t1. Mengubah Data Pasien\n"
             "\t2. Kembali ke Menu utama\n")
        try:
            input_ubah = int(input('Masukkan Menu yang ingin dipilih: '))
        except ValueError:
            print('Inputan tidak valid, silakan masukkan angka')
            continue

        if input_ubah == 1:
            clear_terminal()
            tabel_daftarHewan()
            while True:
                update_kode = str(input('Masukkan kode pasien yang ingin diubah: ')).upper()
                print()
                if update_kode in daftar_pasien['kode']:
                    print('Data pasien ditemukan')
                    print()
                    while True: 
                        confirm_update = input('Apakah anda yakin ingin mengubah pasien ini? (Y/N): ').upper()
                        if confirm_update == 'Y':
                            clear_terminal()
                            print('Pilih Menu yang akan diubah: ')
                            print("\tList Menu: \n"
                                "\t1. Pelayanan\n"
                                "\t2. Status\n"
                                "\t3. Tanggal Keluar\n")
                            while True:
                                try:
                                    pilih_update = int(input('Masukkan menu yang ingin dipilih: '))
                                except ValueError:
                                    print('Inputan tidak valid, silakan masukkan angka 1-3')
                                    print()
                                    continue

                                if pilih_update == 1:
                                    index = daftar_pasien['kode'].index(update_kode)
                                    pelayanan_ubah = input('Masukkan pelayanan baru: ')
                                    print()
                                    daftar_pasien['pelayanan'][index] = pelayanan_ubah
                                    print('Pelayanan berhasil diubah')
                                    tabel_daftarHewan()
                            
                                elif pilih_update == 2:
                                    index = daftar_pasien['kode'].index(update_kode)
                                    status_ubah = input('Masukkan status baru: ')
                                    print()
                                    daftar_pasien['status'][index] = status_ubah
                                    print('Status berhasil diubah')
                                    tabel_daftarHewan()

                                elif pilih_update == 3:
                                    while True:
                                        try:
                                            tanggal_ubah = input('Masukkan tanggal keluar (YYYY-MM-DD): ')
                                            print()
                                            tanggal_ubah = datetime.datetime.strptime(tanggal_ubah, '%Y-%m-%d').date() # agar inputan tanggal tidak asal
                                        
                                        except ValueError:
                                            print("Format tanggal salah. Pastikan formatnya YYYY-MM-DD.")
                                            print()
                                            continue

                                        index = daftar_pasien['kode'].index(update_kode)
                                        daftar_pasien['tanggal_keluar'][index] = tanggal_ubah
                                        print('Tanggal keluar berhasil diubah')
                                        tabel_daftarHewan()

                                        break

                                else:
                                    print('Inputan tidak valid, harap masukkan angka 1-3')
                                    print(
                                    )
                                    continue
                                break
                                

                            while True:
                                confirm2 = input('Apakah Anda ingin mengubah data lain? (Y/N): ').upper()
                                if confirm2 == 'Y':
                                    break

                                elif confirm2 == 'N':
                                    print('Anda kembali ke menu utama')
                                    clear_terminal()
                                    return

                                else:
                                    print('Inputan tidak valid, silakan masukkan Y/N')
                                    continue
                        
                            break

                        elif confirm_update == 'N':
                            print('Tidak jadi merubah data')
                            clear_terminal()
                            break 

                        else:
                            print('Menu yang dipilih tidak ada, silakan pilih lagi')
                            print()
                            continue
                    
                    break 

                else:
                    print('Kode pasien tidak ditemukan')
                    print()
                    continue
                
        elif input_ubah == 2:
            clear_terminal()
            break

        else: 
            print('Inputan tidak valid, silakan masukkan angka 1-2')
            continue

# menu untuk melihat riwayat pasien yang dihapus
def riwayat():
    clear_terminal()
    while True:
        print("\t\nList Menu: \n"
              "\t1. Menampilkan Daftar Riwayat Pasien\n"
                "\t2. Kembali ke Menu utama\n")
        try: # agar disaat input menu selain angka yang ada dipilihan/input str program tidak eror
            input_rwy = int(input('Masukkan Menu yang ingin dipilih: '))
        except ValueError:
            print('Inputan tidak valid, silakan masukkan angka (1-2)')
            continue
        print()

        if input_rwy == 1:
            print('Riwayat Pasien')
            print(tabulate(rwy, headers=headers1, tablefmt='grid').title())
        
        elif input_rwy == 2:
            clear_terminal()
            break
        

def Menu_utama ():
    pw = '81101'
    while True:
        x = input('Masukkan password admin: ')
        if x !=pw:
            print("masukan password ulang")
            continue
        while x == pw:
            print('Data Pasien Klinik Hewan Bahagia')
            print("\tList Menu: \n"
                "\t1. Menampilkan Daftar Pasien\n"
                "\t2. Menambah Pasien\n"
                "\t3. Menghapus Pasien\n"
                "\t4. Mengupdate Pasien\n"
                "\t5. Riwayat Pasien\n"
                "\t6. Exit Program")
        
            try:
                menu = int(input('Masukkan angka Menu yang ingin dijalankan: '))
            except ValueError:
                print('Input tidak valid, silakan masukkan angka')
                continue

            if menu == 1:
                menu_daftar() 
        
            elif menu == 2:
                tambah()
        
            elif menu == 3:
                hapus()

            elif menu == 4:
                ubah()
        
            elif menu == 5:
                riwayat()

            elif menu == 6:
                print('Terimakasih, Anda sudah keluar')
                break
        
            else:
                print('Pilihan Menu tidak valid')
                continue
    
        break

Menu_utama()
