dataBarang = []
print ('=================')
print ('DATA BARANG')
print ('-----------------')
print ('')

while True: 
    print ('Menu: ')
    print ('1. Tambah Data')
    print ('2. Hapus Data')
    print ('3. Tampil Data')
    print ('4. Exit')
    print ('')
    ans = int (input ('Pilihan Menu: '))
    print ('-------------------')

    if ans == 1:
        newData = input ('Masukan Data: ')
        dataBarang.append (newData)
        print ('---------')
        print ('')
    elif ans == 2:
        delData = input ('Data yang dihapus: ')
        dataBarang.remove (delData)
        print ('---------')
        print ('')
    elif ans == 3:
        print ('Data Barang:')
        for data in dataBarang:
            print (data)
        print ('---------')
        print ('')
    else:
        break