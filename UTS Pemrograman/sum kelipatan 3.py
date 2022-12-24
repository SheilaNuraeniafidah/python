a = int(input("enter a:"))
b = int(input("enter b:"))
if( a % 3 == 0):
    num = a
elif (a % 3 == 1):
    num = a + 1
elif ( a % 3 == 2):
    num = a + 1

x = range(num, b , 3)
for p in x:
    print(p)
print("----------+")
print(sum(x))

    
    

    
