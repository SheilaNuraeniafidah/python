import random
num = random.randint(1,100)
num1 = 0
print("hello iam mr.laptop ill give you num between 1-100")
while num1 != num:
    num1 = int(input("enter your guess number:"))
    if num1 > num:
        print("your guess is too high")
    elif num1 < num:
        print("your guess is too low")
    else:
        print("you're right s")