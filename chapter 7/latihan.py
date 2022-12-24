sum = 0
n = 0
while True:
    try:
        num = int(input("Enter an integer: "))
        sum = sum + num
        n = n + 1

        ans = input("Try again (y/n)  ? ")
    except ValueError:
        print("invalid integer")
        
    if ans == "n":
        break

avg = sum / n
print("The average is: ", avg)