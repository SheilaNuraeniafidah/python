try:
    bilangan = open("d:/data1.txt", "r")
    bil1 = int(bilangan.readline())
    bil2 = int(bilangan.readline())

    result = bil1 / bil2

    print(bil1, "dibagi", bil2, "adalah", result)

except FileNotFoundError:
    print("file cannot found")

except ZeroDivisionError:
    print("cannot division by zero")
