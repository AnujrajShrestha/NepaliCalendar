import random
import time

print("Welcome to number gusser game".center(30))
time.sleep(1)

def guess(input1):
    guess=random.randint(1,10)
    if guess==input1:
        print("You won the game".center(30))
    else:
        print("You lose the game")
        print(guess)

while True:
    input1=int(input("Pick the number between (1 to 10) "))
    guess(input1)
    time.sleep(1)
    again=input("Do you want to play again(Y/N) ")
    again1=again.upper()
    if again1=="Y":
        pass
    else:
        break



