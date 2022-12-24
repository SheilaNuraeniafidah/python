def starFormation2(n):
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

starFormation2(4)