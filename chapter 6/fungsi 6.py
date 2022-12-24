#define a non void function
def sumOfTwo(a , b):
    result = a + b
    return result

#call the funtion inside a expression
result = sumOfTwo(10, 20) + sumOfTwo(20, 30)
print(result)

#call the funtion inside a print
print (sumOfTwo(30, 40))