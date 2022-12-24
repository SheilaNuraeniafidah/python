fo = open("d:/studentprofile.txt", "a")

id = input("enter student id:")
name = input("enter student name:")
orgn = input ("enter place of birth:")
birth = input("enter date of birth:")
adrs = input("enter student address:")
gnder = input("enter student gender:")

data = id +"#" + name + "#" + orgn + "#" + birth + "#" + adrs + "#" + gnder

data2 = fo.write('data\n')

print(data2)