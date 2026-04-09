import random
import time

length=int(input("Enter the length of the password "))

password="abcdefghijklmnopqrstuwxyz"
capital=input("Do want to add capital letters(Y/N) ")
capital=capital.upper()
if capital=="Y":
    password+="ABCDEFGHIJKLMNOPQRSTUWXYZ"

number=input("Do you want to add anumbers(Y/N) ")
number=number.upper()
if number=="Y":
    password+="0123456789"

symbols=input("Do you want to add symbols(Y/N) ")
symbols=symbols.upper()
if symbols=="Y":
    password+="!@#$%^&*?{}[];:'=-_<>"

f_password=""

for A in range(length):
    final_password=password[random.randint(0,length)-1]
    f_password+=final_password
    
time.sleep(3)
print(f"The final password is {f_password}".center(30))