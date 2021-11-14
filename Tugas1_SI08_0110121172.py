# Nama      : Alif Fadhlurrahman
# NIM       : 0110121172
# Kelas     : SI08
# Tugas 1   : Sistem Informasi Dagang (SIDAG)

# Function def untuk mengecek dan akan dipanggil nanti si check_email. 
# - Mengecek apakah masukkan yang dimasukkan benar atau salah.
# - Menggunakan import re, didapat dari google dan di bantu juga oleh Ka Fadli.
def check_email():
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input('Masukkan Email : ')
    if (re.fullmatch(regex, email)): 
        return True # Jika email benar, maka akan berlanjut ke proses yang selanjutnya.
    else:
        print('Email tidak valid. Ulangi.')
        return check_email() # Jika email salah, maka akan diminta masukkan kembali.

# Function def untuk mengecek dan akan dipanggil nanti si check_password.
# - Mengecek apakah masukkan yang dimasukkan benar atau salah.
def check_password():
    character = ['@', "#", '$', '!'] # character adalah varibel untuk masukkan karakter yang harus ada dalam password.
    password = input("Masukkan password : ")
    if len(password) >= 8: # Isi password minimal 8 buah masukkan.
        if any(word.isnumeric() for word in password): # Harus ada angka dalam masukkan password.
            if any(word.islower() for word in password): # Harus ada huruf kapital dalam masukkan password.
                if any(word.isupper() for word in password): # Harus ada huruf kecil dalam masukkan password.
                    if any(word in character for word in password): # Harus ada karakter dari varibel character dalam masukkan password.
                        return True # Jika password benar, maka akan berlanjut ke proses yang selanjutnya.
                    else:
                        print("Password tidak valid. Ulangi.")
                        return check_password() # Jika salah satu karakter dalam variabel character tidak ada dalam masukkan, maka akan diminta masukkan kembali.
                else:
                    print("Password tidak valid. Ulangi.")       
                    return check_password() # Jika tidak ada huruf kecil, maka akan diminta masukkan kembali.
            else:
                print("Password tidak valid. Ulangi.")  
                return check_password() # Jika tidak ada huruf kapital, maka akan diminta masukkan kembali.
        else:
            print("Password tidak valid. Ulangi.")
            return check_password() # Jika tidak ada angka, maka akan diminta masukkan kembali.
    else:
        print("Password tidak valid. Ulangi.")
        return check_password() # Jika panjang atau isi dari password tidak lebih dari sama dengan 8 buah masukkan, maka akan diminta masukkan kembali.

# Function def untuk mengecek dan akan dipanggil nanti si check_level_player.
# - Mengecek apakah masukkan benar atau sala.
# - Membuat perhitungan diskon dan harga yang harus dibayarkan nanti diakhir.
def check_level_player():
    discon = 0
    level = input("Masukkan level kepersertaan Anda (Silver/Gold/Diamond) : ")
    while level != 'Silver' and level != 'Gold' and level != 'Diamond': # Jika level yang dimasukkan tidak sesuai dengan ketentuan,
        print("Masukkan tidak valid. Ulangi.") # maka tidak valid
        return check_level_player() # dan akan diminta masukkan ulang.
    else:
        if level == 'Silver':
            if mateials < 5:
                discon = price * (5/100) # Jika barang yang dibeli kurang dari 5,
                print('Selamat! Anda mendapatkan potongan harga 5%') # maka mendapat diskon 5%
            else:
                discon = price * (10/100) # Jika barang yang dibeli lebih dari sama dengan 5,
                print('Selamat! Anda mendapat potongan harga 10%') # maka akan mendapat diskon 10%
        elif level == 'Gold':
            if mateials < 5:
                discon = price * (10/100) # Jika barang yang dibeli kurang dari 5,
                print('Selamat! Anda mendapat potongan harga 10%') # maka mendapat diskon 10%
            else:
                discon = price * (15/100) # Jika barang yang dibeli lebih dari sama dengan 5,
                print('Selamat! Anda mendapat potongan harga 15%') # maka akan mendapat diskon 15%
        elif level == 'Diamond':
            if mateials < 5:
                discon = price * (15/100) # Jika barang yang dibeli kurang dari 5,
                print('Selamat! Anda mendapat potongan harga 15%') # maka mendapat diskon 15%
            else:
                discon = price * (20/100) # Jika barang yang dibeli lebih dari sama dengan 5,
                print('Selamat! Anda mendapat potongan harga 20%') # maka akan mendapat diskon 20%
        after_discon = price - discon # Setelah diskon, maka harga awal akan dikurangi oleh diskon yang didapat.
        print('Total Harga yang harus dibayar : ', float(after_discon)) # Harga yang harus dibayar berbentuk float atau ada titik sebelum angka terakhir harga.
        print("Terima kasih telah berbelanja di NFElectrics!")
        print('\n') 
        quit() # Jika transaksi berhasil dan selesai, maka akan berhenti.       
    
print('\n')
mateials = 0 # Jumlah barang yang akan dibeli nanti.
total_price = 0 # Total harga dari semua barang yang telah dibeli.
print('Fitur Belanja')
print()
while True:
    product = input('Masukkan nama produk yang akan dibeli atau X untuk selesai : ')
    while product == "": # Jika tidak masukkan produk atau langsung ditekan enter,
        product = input("Tidak valid. Masukkan produk : ") # maka akan diminta ulang masukkan produk.
    if product == 'X' or product == 'x': # Jika menekan X atau x, maka selesai untuk memasukkan produk.
        if mateials > 0: # Jika barang yang dimasukkan lebih dari 0, maka:
            print()
            print('Total produk yang dibeli : ' + str(mateials)) # akan mencetak(print) dengan nama produknya
            print('Total harga produk : ', float(total_price)) # dan akan mentak(print) dengan harganya
            print()
            membership = input('Apakah Anda seorang anggota? (Y/T) : ') # Diminta masukkan keanggotaan.
            if membership == 'T' or membership == "t": # Jika bukan seorang anggota, maka:
                print('Total harga yang harus dibayar : ', float(total_price)) # akan dicetak(print) dengan total harga yang harus dibayar
                print("Terima kasih telah berbelanja di NFElectrics!") # dan transaksi akan selesai.
                print('\n')
                quit()
            elif membership == 'Y' or membership == 'y': # Tetapi jika dia seorang anggota, maka
                check_email() # panggil def check_email dan akan dijalankan sesuai ketentuan.
                while True: # Sementara kalau benar,
                    if check_password(): # akan langsung mengecek password, dan jika password benar, maka
                        check_level_player() # akan diminta untuk memaukkan level kepersertaan.
                    else:
                        check_password() # Jika salah, akan diminta masukkan ulang.
            else:
                quit() # Jika dia bukan seorang anggota maka akan berhenti.
        elif product == "X" or product == "x" and mateials == 0: # Jika tidak ada produk dan harga yang dimasukkan maka,
            print("Terima kasih telah berkunjung di toko Kami. Sampai jumpa!") # akan dicetak(print)
            print('\n')
            quit() # dan transaksi selesai atau tidak jadi berbelanja.
    else: 
        price = int(input('Masukkan harga produk : ')) # Ketika tadi menekan X atau x, maka akan diminta masukkan harga produk.
        print('Berhasil menambahkan', product, 'dengan harga', float(price))
        mateials += 1 # Barang akan bertambah jika masukkan produknya terus dijalankan dan tidak ada infinite loop.
        total_price += price # Total harga akan bertamnah jika masukkan harganya terus dijalankan dan tidak ada infinite loop.