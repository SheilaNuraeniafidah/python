fo = open("d:/mydata.txt", "a")
fo.write("solo")

fo = open("d:/mydata.txt", "r")
data = fo.read()
print(data)

fo.close()