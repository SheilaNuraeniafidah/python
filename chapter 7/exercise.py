n = int(input("\n enter an integer number: "))
data = []
jum = 0

for i in range (n):
    temp = int(input("Masukkan data ke-%d: " % (i+1)))
    data.append(temp)
    jum += data[i]
    rata2 = jum / n

print("\nRata-rata  = %0.2f" % rata2)
