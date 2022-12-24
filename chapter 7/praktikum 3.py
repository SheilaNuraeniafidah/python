try:
    file = open("d:/data2", "r")
    sum = 0

    for data2 in sum:
        sum = sum + int(data2)
    print(sum)
except FileNotFoundError:
    print("file not found")