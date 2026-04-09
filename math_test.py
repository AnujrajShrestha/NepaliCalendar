import random
import os
import time

print("Maths Test".center(50))
time.sleep(2)
os.system('cls')
time.sleep(1)
rand_1=random.randint(1,50)
rand_2=random.randint(1,50)
rand_3=["+","-","*"]
rand=random.choice(rand_3)

if rand=="+":
    calculate=rand_1 + rand_2
elif rand=="-":
    calculate=rand_1-rand_2
elif rand=="*":
    calculate=rand_1*rand_2

chance=5
for chances in range(0,5,1):
    print(f"{rand_1} {rand} {rand_2}")
    answer=int(input("Enter the answer "))
    if answer==calculate:
        print("corect answer")
        break
    else:
        print("Wrong answer")
        chance-=1
        print(f"Chaces:{chance}")

if chance==0:
    time.sleep(1)
    os.system('cls')
    print("You lose the game".center(50))
    print(f"The answer is {calculate}")