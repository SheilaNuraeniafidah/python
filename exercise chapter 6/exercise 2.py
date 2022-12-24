def starFormation1(n):
    a = 0
    b = 1
    for i in range (n):
        while (a != b):
            print("*", end= "")
            a += 1
        print('')
        a = 0
        b += 1

starFormation1(4)
