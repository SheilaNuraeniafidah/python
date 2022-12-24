#example 1
def myfunction():
    a = 4
a = 10

myfunction()
print(a)

#example 2
def myfunction1():
    global a
    a = 4
a = 10
myfunction1()
print(a)