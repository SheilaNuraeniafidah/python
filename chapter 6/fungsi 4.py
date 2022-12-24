#having default value in argument
def sumOfThree(a, b, c=0):
    result = a + b + c
    print("the result is", result)

#call the function
sumOfThree(10, 20, 30)
sumOfThree(10, 20)