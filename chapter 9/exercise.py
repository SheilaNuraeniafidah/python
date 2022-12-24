fo = open("d:/semester 1/pemrograman terstruktur/python/students.dat", "r")
datastudent = fo.readlines()
countMale = 0
countFemale = 0

print("-------------------------------------------------------------------------------------------")
print("ID       NAME      ADDRESS   BIRTH DATE   BIRTH PLACE GENDER")
print("-------------------------------------------------------------------------------------------")

for data in datastudent:
    data = data.strip()
    splitted = data.split("#")
    if (splitted[5] == "M"):
        countMale += 1
    elif(splitted[5] == "F"):
        countFemale += 1
    print(splitted[0], splitted[1].ljust(9), splitted[2].ljust(9),splitted[3].ljust(12),splitted[4].ljust(12), splitted[5].ljust(30))

print("------------------------------------------------------------------------------------------")
print("number of male student   :", countMale)
print("number of female student :", countFemale)
print("------------------------------------------------------------------------------------------")
print("total student            :", countMale + countFemale)
print("------------------------------------------------------------------------------------------")

fo.close()
