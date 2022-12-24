biaya = 200000
print("total biaya rental mobil")
WaktuSewa= int(input("masukkan jam sewa:"))
waktuSelesai= int(input("masukkan jam selesai:"))
totalWaktu = waktuSelesai - WaktuSewa 
if(totalWaktu == 12):
    print('biaya sewa anda 200000')
elif(totalWaktu > 12):
    print('biaya sewa anda', totalWaktu * 200000 + 10000)
elif(totalWaktu < 12):
    print("biaya sewa anda", totalWaktu*200000-10000)