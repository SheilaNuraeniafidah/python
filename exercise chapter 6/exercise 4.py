def starformation3(n):
    n = n // 2 + 1
    a = 0
    b = 1
    for i in range (n):
        while (a != b):
            print("*", end= "")
            a += 1
        print('')
        a = 0
        b += 1

    n -= 1
    a = n
    b = 1
    for i in range (n):
        while (a !=0):
            print("*", end= "")
            a -= 1
        print ("")
        a = n
        a -= b
        b += 1


starformation3(7)
