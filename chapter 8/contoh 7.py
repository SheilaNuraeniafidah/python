fo = open("d:/mydata.txt", "a+")

fo.write("solo\n")
data = fo.read()
print(data)

fo.close

#solution

fo = open ("d:/mydata.txt", "a+")
fo.write("hello solo\n")
fo.seek(0)
data = fo.read()
print(data)
fo.close