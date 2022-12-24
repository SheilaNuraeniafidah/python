try:
    buka = open("d:/myfile.txt", "r")
    data = buka.read()
    print(data)

except FileNotFoundError:
    print("sorry this file couldn't found")