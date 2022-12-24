try:
    num1 = int(input("enter an integer number:"))
    num2 = int(input("enter another integer number:"))
    result = num1/num2
    print("the result of division is:",result)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("the number must an integer")