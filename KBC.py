import time
import os

time.sleep(1.5)
print("Wellcome to KBC".center(55))
time.sleep(1.5)
os.system('cls')
time.sleep(1.5)
money=0

print ("1.What is capital city of Nepal")
print()
time.sleep(1)
frist_question=["Kathmandu","Butwal","Pokhara","Gulmi"]
print(frist_question)
time.sleep(1)
frist_answer=input("Enter the answer ")
frist_answer=frist_answer.upper()
if frist_answer==frist_question[0].upper():
    time.sleep(1)
    print("Correct answer")
    money+=5000
    time.sleep(1)
    print(f'current won price:{money}')
else:
    time.sleep(1)
    print ("Worng answer")
    time.sleep(1)
    print(f'Current won price: {money}')
time.sleep(1)
os.system('cls')
time.sleep(1)
print ("2.What is first genration of computer")
time.sleep(1)
second_question=["Bio chip","Vacuum tube","Transistor","Micro chip"]
time.sleep(1)
print(second_question)
time.sleep(1)
second_answer=input("Enter the answer ")
second_answer=second_answer.upper()
if second_answer ==second_question[1].upper():
    time.sleep(1)
    print ("Correct answer")
    money+=10000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print("Wrong answer")
    money-=2500
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1)
os.system('cls')
time.sleep(1)
print("3.What is the leatest graphics")
time.sleep(1)
third_question=["RTX3090","RTX2090","RTX3060","RTX4090"]
print(third_question)
third_answer=input("Enter the answer ")
third_answer=third_answer.upper()
if third_answer==third_question[3].upper():
    time.sleep(1)
    print ("Correct answer")
    money+=15000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print ("Wrong answer")
    money-=5000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("4.What is the leatest gen of ram")
time.sleep(1)
fouth_question=["DDR1","DDR3","DDR5","DDR6"]
print(fouth_question)
fouth_answer=input("Enter the answer ")
fouth_answer=fouth_answer.upper()
if fouth_answer==fouth_question[2].upper():
    time.sleep(1)
    print("Correct answer")
    money+=20000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print ("Wrong answer")
    money-=7500
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("5.What is hight of  Mt.Everest")
time.sleep(1)
fifth_question=["6798KM","8823KM","8867KM","8848KM"]
print(fifth_question)
time.sleep(1)
fifth_answer=input("Enter the answer ")
fifth_answer=fifth_answer.upper()
if fifth_answer==fifth_question[3].upper():
    time.sleep(1)
    print("Correct answer")
    money+=25000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print ("Wrong answer")
    money-=10000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("6.What is capital city of Australia")
sixth_question=["Paris","Kathmandu","Canberra","France"]
time.sleep(1)
print(sixth_question)
time.sleep(1)
sixth_answer=input("Enter the answer ")
sixth_answer=sixth_answer.upper()
if sixth_answer==sixth_question[2].upper():
    time.sleep(1)
    print ("Correct answer")
    money+=30000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print ("Wrong answer")
    money-=15000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("7.What chemical symbol of gold")
seventh_question=["Ag","Au","H2O","HOC"]
time.sleep(1)
print(seventh_question)
time.sleep(1)
seventh_answer=input("Enter the answer ")
if seventh_answer==seventh_question[1]:
    time.sleep(1)
    print("Correct answer")
    money+=35000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print("Wrong answer")
    money-=20000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("8.When was the first iPhone released")
eigth_question=[2011,2009,2007,2012]
time.sleep(1)
print(eigth_question)
time.sleep(1)
eigth_answer=int(input("Enter the answer "))
if eigth_answer==eigth_question[2]:
    time.sleep(1)
    print ("Correct answer")
    money+=40000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print("Wrong answer")
    money-=25000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print("9.Which planet is known as the (The red planet) ")
ninth_question=["Mars","Jupiter","Earth","Uranus"]
time.sleep(1)
print(ninth_question)
time.sleep(1)
ninth_answer=input("Enter the answer ")
ninth_answer=ninth_answer.upper()
if ninth_answer==ninth_question[0].upper():
    time.sleep(1)
    print ("Correct answer")
    money+=45000
    time.sleep(1)
    print(f'Current won price:{money}')
else:
    time.sleep(1)
    print("Wrong answer")
    money-=30000
    time.sleep(1)
    print(f'Current won price:{money}')
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print ("10.Who discovered electricity")
time.sleep(1)
tenth_question=["Issac newton","Benjamin Franklin","Nekola Tesla","Andrew Tate"]
time.sleep(1)
print(tenth_question)
time.sleep(1)
tenth_answer=input("Enter the answer ")
tenth_answer=tenth_answer.upper()
if tenth_answer==tenth_answer[1].upper():
    time.sleep(1)
    print ("Correct answer")
    money+=50000
else:
    time.sleep(1)
    print ("Wrong answer")
    money-=35000
time.sleep(1.5)
os.system('cls')
time.sleep(1)
print (f"you won {money}".center(55))
time.sleep(4)
