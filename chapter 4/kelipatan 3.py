a = int(input("masukkan nilai minimum"))
b = int(input("masukkan nilai maksimum"))
if( a % 3 == 0):
    num = a
elif (a % 3 == 1):
    num = a + 1
elif ( a % 3 == 2):
    num = a + 2

x = range(num, b + 1, 3)
for p in x:
    print(p)
