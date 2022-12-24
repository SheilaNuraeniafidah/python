import math

def isPhytagoras():
    while True:
        a = int(input("a =  "))
        b = int(input("b =  "))
        c = int(input("c =  "))
        p = int(math.sqrt(a**2 + b**2))
        if c == p:
            x = [a,b,c]
            print(x,"----->", True)
        else:
            x = [a,b,c]
            print (x,"----->", False)
        
isPhytagoras()


          