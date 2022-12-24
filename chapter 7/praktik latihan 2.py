try:
    while True:
        a = input("masukkan nama file:")
        file = open("a", "r")
        file = str(a.read())
        b = input("data yang mau ditambahkan:")
        file1 = open("file", "a")
        file1.write()
        file2 = str(file1.read())
        c = input("mau lagi(y/n):")
        if c == "n":
            file1.closed

    print(file2)

except FileNotFoundError:
    print ("file cannot found")
