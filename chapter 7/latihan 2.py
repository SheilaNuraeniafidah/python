def division (a,b):
    try:
        result = a/b
        print ("the result is:", result)
    except ZeroDivisionError:
        print ("division not valid")

division(8,3)
division(9,0)
division(3,4)