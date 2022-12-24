try :
    z = input("masukkan nama file:")
    x = open(z.read())

    print("isi file",z, "adalah", x)

except AttributeError:
    print("incorrect input or file cannot found")