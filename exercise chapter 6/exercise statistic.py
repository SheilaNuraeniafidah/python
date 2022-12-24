def summation (*args):
    result = sum (args)
    return result

def average (*args):
    result =  sum (args) // len(args)
    return result

def maximum (*args):
    result = max (args)
    return result

def minimum (*args):
    result = min (args)
    return result

def statistic (*args):
    print (summation (*args))
    print (average (*args))
    print (maximum (*args))
    print (minimum (*args))


a = (5, 10, 4, 9, 30, 16, 2, 11)
b = (81, 98, 12, 83, 45, 77, 69, 30, 56)

print ("statistic a")
statistic (*a)
print ("statistic b")
statistic (*b)