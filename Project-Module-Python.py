# # # # create

dataobat = [
    {
        'Kode Obat' : '101',
        'Nama Obat' : 'Amoxillin 150 Mg',
        'Jenis Obat' :'Generik',
        'Stok Obat' : 75,
        'Harga' : 5000,
        'Tanggal Expired' : '27/12/2023',
    },
    {
        'Kode Obat' : '102',
        'Nama Obat' : 'Paracetamol 500 Mg',
        'Jenis Obat' : 'Generik',
        'Stok Obat' : 124,
        'Harga' : 3000,
        'Tanggal Expired' : '01/01/2024',
    },
    {
        'Kode Obat' : '103',
        'Nama Obat' : '88 Salep Botol',
        'Jenis Obat' : 'Keras',
        'Stok Obat' : 10,
        'Harga' : 13500,
        'Tanggal Expired' : '13/11/2023',
    },
    {   'Kode Obat' : '104',
        'Nama Obat' : 'Vit B Complex 5 mg',
        'Jenis Obat' : 'Vitamin',
        'Stok Obat' : 43,
        'Harga' : 3000,
        'Tanggal Expired' : '07/05/2024'
    },
    {'Kode Obat' : '105',
        'Nama Obat' : 'Tolak Angin 100 ml',
        'Jenis Obat' : 'Herbal',
        'Stok Obat' : 124,
        'Harga' : 3000,
        'Tanggal Expired' : '06/03/2024'
    }
]


# Variabel kosong sementara
cart=[] 
DatabasePembeli =[]
Nopembeli = 0 


# Fungsi template tabel database Pembeli Obat
def Pembeli (listData0):
    print('\t ========================== Daftar Pembeli ========================== ')
    print('\tNo Pembeli\t| Nama Pembeli \t\t| Nama Obat \t\t\t| Qty\t\t| Kode Obat \t\t| Harga |' )
    for i in range(len(listData0)) :
        print('\t{}\t\t| {} \t\t| {} \t\t| {}\t\t| {} \t\t\t| {}'.format(listData0[i]['No Pembeli'],listData0[i]['Nama Pembeli'],listData0[i]['Nama Obat'],listData0[i]['Qty'],listData0[i]['Kode Obat'],listData0[i]['Harga']))

    for item in cart:
        print(f'{item[0]}\t\t|{item[1]}\t\t|{item[2]}\t\t|{item[3]}\t\t|    {item[4]}   |{item[5]}\t\t')
    return    

# Fungsi template tabel daftar Obat
def ShowList (listData):
    print('\t ================================ Daftar Stok Obat ================================')
    print('\tKode Obat\t| Nama Obat \t\t\t| Jenis Obat  \t\t\t| Stok Obat   \t| Harga  \t| Tanggal Expired')
    for i in range(len(listData)) :
        print('\t{}\t\t| {}  \t\t| {}  \t\t\t| {}  \t\t| {}\t\t| {} \t'.format(listData[i]['Kode Obat'],listData[i]['Nama Obat'],listData[i]['Jenis Obat'],listData[i]['Stok Obat'],listData[i]['Harga'],listData[i]['Tanggal Expired']))

# Fungsi update barang sesuai kolom
def UpdateBarang(Data, Kolom,NewData2):
    InputUpdateBarang= (input("\tApakah data yang diupdate sudah benar? (Ya/Tidak): ")).lower()
    if InputUpdateBarang == "ya":
        Data[0][Kolom] = NewData2
        print("\n\tData sudah diperbarui!, Silahkan cek data terupdate pada menu 2")
    else:
        print("\t Data tidak terupdate!")

# # Fungsi template tabel keranjang
def cartfung(listData2):
    print('\t ============ Daftar Keranjang ============ ')
    print('\tNama Obat\t\t\t| Qty \t\t\t| Kode Obat ')
    for i in range(len(listData2)):
        print('\t{}\t\t| {} \t\t\t| {}'.format(listData2[i]['Nama Obat'],listData2[i]['Qty'],listData2[i]['Kode Obat']))

# Fungsi filter dictionary dalam list
def SearchList(Input):
    SearchList = (list(filter(lambda data: data['Kode Obat'] == str(Input), dataobat)))
    return SearchList

# Pilihan untuk menampilkan seluruh Stok Obat dalam databases
def MenuDataObat():
    while True:
        print('''
        ==== Menu Menampilkan Stok Obat ====
        
        1. Menampilkan semua Stok Obat
        2. Menampilkan data tertentu
        3. Kembali ke menu utama\n ''')

        SubMenu = int(input('''Silahkan pilih daftar diatas [1-3]: '''))
        if SubMenu == 1 and len(dataobat):
            ShowList(dataobat)
        elif SubMenu == 2 and len(dataobat):
            CodeStok = (input("\tMasukkan Kode Obat yang ingin anda cari: "))
            SearchList(CodeStok)
            if len(SearchList(CodeStok)):
                ShowList(SearchList(CodeStok))
            else:
                print("\n\t Data Tidak Ditemukan")
        elif SubMenu == 3:
            MenuAwal()
        else :
            print('\nSilahkan masukkan pilihan yang sesuai [1-3]:')
            continue  

# Pilihan untuk Menambah Stok Obat
def MenambahData():
    while True:
        CreateData = input('''
        **********Menu Menambah Stok Obat***********
        
                1. Menambah Stok Obat ke database
                2. Kembali ke menu utama
        Silahkan pilih menu diatas : ''')

        if CreateData == '1':
            ShowList(dataobat)
            KodeObat = int(input('\nMasukkan Kode Obat baru : '))
            for i in range(len(dataobat)):
                if KodeObat == dataobat[i]['Kode Obat']:
                    print('Data sudah ada didalam database, silahkan masukkan data baru')
                    MenambahData()
                elif(i == len(dataobat) - 1) and(KodeObat != dataobat[i]['Kode Obat']):    
                    Nama = input('Nama Obat: ').capitalize()
                    Jenis = input('Jenis Obat: ').capitalize()
                    Stok = int(input('Stok Obat: '))
                    Harga = input('Harga: ')
                    Tanggal = input('Tanngal Expired: ')
                    break
            Konfirmasi = input('''Apakah anda yakin data ini akan ditambahkan (Y/T)? : ''').capitalize()
            if Konfirmasi == 'Y':
                dataobat.append({
                    'Kode Obat': KodeObat,
                    'Nama Obat': Nama,
                    'Jenis Obat': Jenis,
                    'Stok Obat': Stok,
                    'Harga': Harga,
                    'Tanggal Expired': Tanggal,
                })
                ShowList(dataobat)
                print('\n Stok Obat Berhasil ditambahkan')
                MenambahData()
                continue
            elif Konfirmasi == 'T':
                print('\nData Obat Tidak Jadi ditambahkan')
                MenambahData()
        elif CreateData == '2':
            MenuAwal()
        else:
            print('''\nPilihan yang anda masukkan salah, Silahkan Masukkan pilihan range [1-2]''')
            continue

# Menu Untuk Update/Mengubah stok Obat
def UpdateData():
    while True:
        Updatedatacust = input('''
        ======= Menu ubah data customer ======
                
            1. Update Stok Obat
            2. Cek data terupdate
            3. Kembali ke main menu
        
        Silahkan pilih menu diatas ''')

        if Updatedatacust == '1':
            ShowList(dataobat)
            CodeObat = ((input('\n===Masukkan Kode Stok Obat:')))
            for i in range(len(dataobat)):
                if CodeObat == dataobat[i]['Kode Obat']:
                    while True:
                        print('''
                              === Data Obat ditemukan === ''')
                        SearchList(CodeObat)
                        ShowList(SearchList(CodeObat))
                        Konfirmasi = input('''
                        === Apakah data ingin di ubah (Y/T)? : ''').capitalize()
                        if Konfirmasi == 'Y':
                            kolom = int(input('''\tKategori Database Stok Obat
                                              1. Kode Obat
                                              2. Nama Obat
                                              3. Jenis Obat
                                              4. Stok Obat
                                              5. Harga
                                              6. Tanggal Expired
                                              Masukkan kolom data yang ingin diubah:  '''))
                            if kolom == 1:
                                MasukkanData = input("\tMasukkan data baru: ")
                                UpdateBarang(SearchList(CodeObat), 'Kode Obat', MasukkanData)
                            elif kolom == 2:
                                MasukkanData = input("\tMasukkan data baru: ").capitalize()
                                UpdateBarang(SearchList(CodeObat), 'Nama Obat', MasukkanData)
                            elif kolom == 3:
                                MasukkanData = input("\tMasukkan data baru: ").capitalize()
                                UpdateBarang(SearchList(CodeObat), 'Jenis Obat', MasukkanData)
                            elif kolom == 4:
                                MasukkanData = input("\tMasukkan data baru: ")
                                UpdateBarang(SearchList(CodeObat), 'Stok Obat', MasukkanData)
                            elif kolom == 5:
                                MasukkanData = input("\tMasukkan data baru: ")
                                UpdateBarang(SearchList(CodeObat), 'Harga Obat', MasukkanData)
                            else:
                                MasukkanData = input("\tMasukkan data baru: ")
                                UpdateBarang(SearchList(CodeObat), 'Tanggal Expired', MasukkanData)
                            break
        elif Updatedatacust == '2':
            ShowList(dataobat)
        elif Updatedatacust == '3':
            MenuAwal()
        else:
            print('\n\nMasukkan yang anda input salah, silahkan input nomor dari range 1 - 3')

# Fungsi menghapus daftar Obat dari databases
def DeleteData():
    inputDel = (int(input('''
        Menu Menghapus Daftar Obat:
            1. Menghapus Daftar Obat dari stok data
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputDel == 1:
        ShowList(dataobat)
        DelKodeID = (input("\n\tMasukkan Kode Obat yang ingin dihapus:"))
        ListValue2 = [value2 for dataku in dataobat for value2 in dataku.values()]
        if DelKodeID not in ListValue2:
            print("\n\tData yang ingin anda hapus tidak ada!")
        else:
            SearchList(DelKodeID)
            ShowList(SearchList(DelKodeID))
            hapus = (input("\n\t Hapus Data (Ya/Tidak)?")).lower()
            if hapus == "ya":            
                for e in SearchList(DelKodeID) :
                    dataobat.remove(e)
                print("\n\t Data berhasil terhapus!")
                ShowList(dataobat)
            else: 
                print("\n\t Data tidak berhasil terhapus!")
    elif inputDel == 2:
        MenuAwal() 
    DeleteData()

# Fungsi tambahan membeli obat
def Buy():
    inputBuy = (int(input('''
        Menu Membeli Obat:
            1. Membeli Obat
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputBuy == 1:
        ShowList(dataobat)
        while True:
            inputbeli = (input("\n\tMasukkan Kode Obat yang Anda cari: "))
            ListValue3 = [value3 for dataku in dataobat for value3 in dataku.values()]
            if inputbeli not in ListValue3:
                print("\n\tObat yang ingin anda beli sedang tidak tersedia!")
                Buy()
            else:
                print("\t Data Obat yang ingin Anda Beli:")
                Var = SearchList(inputbeli)
                ShowList(Var)
                tambahkan = (input('\n\t Tambahkan daftar Obat kedalam keranjang? (Ya/Tidak):')).lower() 
                if tambahkan == 'ya':
                    Qty = int(input('\t Berapa banyak Obat yang anda inginkan?: '))
                    if Qty > Var[0]['Stok Obat']:
                        print("\n\t Mohon maaf stok Obat tidak cukup")
                        cart.clear()
                    else:
                        cart.append({'Nama Obat': (Var[0]['Nama Obat']),
                                     'Harga': (Var[0]['Harga']),
                    'Qty': Qty,
                    'Kode Obat': (Var[0]['Kode Obat'])
                    })
                else:
                    print("\n\t Keranjang tidak ter-update!")
                    cart.clear()
                    Buy()
                
            cartfung(cart)
            checker = (input('\tMau beli obat yang lain? (ya/tidak) :')).lower()
            if (checker == 'ya') :
                True
            else:
                break
            
        cartfung(cart)   
        CheckOut = (input("\t Lanjutkan check out? (Ya/Tidak): " )).lower()
        if CheckOut == "tidak":
            print("\t Tidak jadi membeli!")
            cart.clear()
            Buy()
        elif CheckOut == "ya":
            global Nopembeli
            NamaPembeli = (input("\tMasukkan Nama Anda:"))
            print(f"""\t\n  ======== No Pembeli Anda adalah: {Nopembeli} ========"""
            )
            Nopembeli = Nopembeli
            Nopembeli+= 1
            penampungansementara = {"No Pembeli":Nopembeli, "Nama Pembeli": NamaPembeli}
            for item in range(len(cart)):
                cart[item].update(penampungansementara)
            DatabasePembeli.extend(cart)
            print("\n\n\t = = = =  Minum Obat Sesuai anjuran Dokter xxxxx \n\t\t xxxxxxx Semoga Lekas Sembuh!!! = = = =!")
            for item in cart:
                (SearchList(item['Kode Obat']))[0]['Stok Obat']-=item['Qty']
            print("\n\t info: Stok Obat terupdate!")
        else: 
            cart.clear()
            
        cart.clear()
        ShowList(dataobat)
        print("\n")
        Pembeli(DatabasePembeli)
    elif inputBuy == 2:
        MenuAwal()
    Buy()

# Menu Utama
def MenuAwal():
    print('''
     = = = = = = =Selamat Datang Di Apotek Berkah Ibu = = = = = = = 

        = = = = = = = = = Daftar Pilihan : = = = = = = = =
            
            1. Report Stok Obat
            2. Menambahkan Data Stok Obat
            3. Mengupdate Data Stok Obat
            4. Menghapus Data
            5. Membeli Obat
            6. Exit ''')

    while True:

        PilihanMenu = (input('\nMasukkan nomor yang dipilih[1-5]: '))
        if PilihanMenu == '1':
            MenuDataObat()
        elif PilihanMenu == '2':
            MenambahData()
        elif PilihanMenu == '3':
            UpdateData()
        elif PilihanMenu == '4':
            DeleteData()
        elif PilihanMenu == '5':
            Buy()
        elif PilihanMenu == '6':
            print('\n=== Terima kasih Cepat Sembuh dan Sampai Jumpa lagi :) === \n')
            exit()
        else:
            print('Anda memasukkan pilihan yang salah \nsilahkan pilih menu yang benar antara [1-5] ')  
MenuAwal()       


















# # # Car_Rental_Jaya = {'Agreement': [24, 31, 43, 54, 65, 71], 
# # #                     'Mobil' : ['Yaris', 'Innova', 'Avanza', 'Kijang', 'Mercedes', 'BMW'],
# # #                     'Lama_Sewa(hari)' : [4, 5, 2, 1, 10, 7],
# # #                     'Biaya_Per_Hari' : [350000, 500000, 400000, 550000, 800000, 750000]}

# # # print(Car_Rental_Jaya)