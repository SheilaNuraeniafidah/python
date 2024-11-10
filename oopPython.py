class Mahasiswa:
    # atribut
    nim = ""
    nama = ""
     
   # method
    def printMhs(self):
        print("NIM Mahasiswa  :", self.nim)
        print("Nama Mahasiswa :", self.nama)

# membuat obyek 'mhs1' dari class Mahasiswa
mhs1 = Mahasiswa()
 
# memberi nilai kedua atribut dari obyek
mhs1.nim = "M01"
mhs1.nama = "Rosihan Ari"
 
# memanggil method
mhs1.printMhs()


#oopPythonConstructor
class Mahasiswa:
    nim = ""
    nama = ""
     
    # constructor
    def __init__(self, x, y):
        self.nim = x
        self.nama = y
     
    def printMhs(self):
        print("NIM Mahasiswa  :", self.nim)
        print("Nama Mahasiswa :", self.nama)
# membuat obyek 'mhs1' dari class Mahasiswa sekaligus memberi nilai atributnya
mhs1 = Mahasiswa("M01", "Rosihan Ari")
 
# memanggil method
mhs1.printMhs()

#overloading oop Python
class Penjumlahan:
     
    # method hasil() dengan variasi parameter
    def hasil(self, *args):
        sum = 0
        for num in args:
            sum += num
        print(sum)
coba = Penjumlahan() 
coba.hasil(1, 2) 

