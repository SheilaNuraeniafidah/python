#contoh 1
fo = open("d:/myfile.txt", "r")
while True:
    data = fo.read(1)
    print(data)
    
    if not data:
        break
fo.close

#contoh 2
fo1 = open("d:/myfile.txt", "r")
data = fo1.readline()
print(data)

    
fo1.close