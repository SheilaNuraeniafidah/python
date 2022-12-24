#contoh 1
fo = open("d:/myfile.txt", "r")
data = fo.read()
print (data)
fo.close

#contoh 2
fo1 = open("d:/myfile.txt", "r+")
data = fo1.read(2)
print(data)
fo1.close