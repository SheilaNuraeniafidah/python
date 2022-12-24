def division (a,b):
    result = a/b
    print("the result is:", result)
try:
    division(8,3)
    division(9,0)
    division(3,4)
except ZeroDivisionError:
    print("division not valid")