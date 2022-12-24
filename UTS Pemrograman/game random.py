import random
score = 0
lives = 5
while True:
    print("what is the result of:")
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    c = a + b
    print(f"{a} + {b}")
    jawab = int(input(">>"))

    if jawab == c:
        score += 10
        print("jawaban benar, skor anda", score,"lives:", lives)

    elif ~(jawab == c )  :
        score -= 2
        lives -= 1 
        print("jawaban salah,skor anda", score,"lives:", lives)

    if(lives == 0):
        print("game over")
        break
