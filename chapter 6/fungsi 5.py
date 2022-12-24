#dynamic argument
def printHello(*words):
    for word in words:
        print("hello", word)

#call the argument
printHello("world", "python","students", "ptik uns")