
#import library
import random


num1 = random.randint(1,100)
num = 0
score = 100

print ("hi..my name is mr. laptop. i have chosen between 1-100. can you guess it?")

while (num != num1):
    num = int(input("enter the number: "))
    
    if (num > num1):
          print ("too high")
          score -= 5
          print ("your score is", score)
    elif (num < num1):
          print ("too low")
          score -= 5
          print ("your score is", score)
          
    else:
        print("you right. your score is", score)
