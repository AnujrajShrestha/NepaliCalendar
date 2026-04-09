import random
import os
import time

while True:
    os.system('cls')
    time.sleep(1)
    print("1.rock")
    print("2.Paper")
    print("3.Scissor")
    time.sleep(1)
    user=int(input("Enter your choice "))
    if user==1:
        user="rock".upper()
    elif user==2:
        user="Paper".upper()
    elif user==3:
        user="scissor".upper()
    else:
        print("Invaild choice")
    ran=["rock","paper","scissor"]
    computure=random.choice(ran)
    computer=computure.upper()
    if computer==user:
        print("Tie")
    elif  (computer=="PAPER" and user=="ROCK") or (computer=="ROCK" and user=="SCISSOR") or (computer=="SCISSOR" and user=="PAPER"):
        print("Computer wins")
    elif (user=="PAPER" and computer=="ROCK") or (user=="ROCK" and computer=="SCISSOR") or (user=="SCISSOR" and computer=="PAPER"):
        print("You win")
    print(f"Player:{user.lower()}  Computer:{computer.lower()}")
    again=input("Do want to play again(Y/N) ")
    again=again.upper()
    if again=="Y":
        pass
    else:
        break


