import os
import time


#starting
def start():
    char="Number system conversion"
    tr=1
    for characters in range(1,len(char)):
        if tr==1:
            character=char[0]
            tr=0
        print(f"{character}".center(180),end="",flush="True")
        character+=char[characters]
        time.sleep(0.025)
        os.system('cls')
    print(char.center(180))
    time.sleep(1.2)
    os.system('cls')
    


def choice():
    print("1.Binary to decimal".center(180))
    time.sleep(0.25)
    print("2.Binary to octal".center(180))
    time.sleep(0.25)
    print("3.Binary to hexadecimal".center(180))
    time.sleep(0.25)
    print("4.Decimal to binary".center(180))
    time.sleep(0.25)
    print("5.Decimal to octal".center(180))
    time.sleep(0.25)
    print("6.Decimal to hexadecimal".center(180))
    time.sleep(0.25)
    print("7.Octal to binary".center(180))
    time.sleep(0.25)
    print("8.Octal to decimal".center(180))
    time.sleep(0.25)
    print("9.Octal to hexadecimal".center(180))
    time.sleep(0.25)
    print("10.Hexadecimal to binary".center(180))
    time.sleep(0.25)
    print("11.Hexadecimal to decimal".center(180))
    time.sleep(0.25)
    print("12.Hexadecimal to octal".center(180))
    time.sleep(0.25)
    enter=int(input("Enter your choice: "))
    match enter:
        case 1:
            #Binary to decimal
            B_to_D()
        case 2:
            #Binary to Octal
            B_to_O()
        case 3:
            #Binary to Hexadecimal
            B_to_H()
        case 4:
            #Decimal to Binary
            D_to_B()
        case 5:
            #Decimal to Octal
            D_to_O()
        case 6:
            #Decimal to Hexadecimal
            D_to_H()
        case 7:
            #Octal to Binary
            O_to_B()
        case 8:
            #Octal to Decimal
            O_to_D()
        case 9:
            #Octal to Hexadecimal
            O_to_H()
        case 10:
            #Hexadecimal to binary
            H_to_B()
        case 11:
            #Hexadecimal to decimal
            H_to_D()
        case 12:
            #Hexadecimal to Octal
            H_to_O()
        case _:
            else_case()

#Binary to decimal
def B_to_D():
    os.system('cls')
    print("Binary to Decimal".center(150))
    enter_1=str(input("Enter the binary number(0 or 1): "))
    base=2
    length=len(enter_1)
    calculate=0
    for calculation in range(0,length,1):
        calculate=calculate+int(enter_1[calculation])*base**(length-calculation-1)
    time.sleep(0.5)
    print(f"The decimal number is: {calculate}")

#Binary to Octal
def B_to_O():
    os.system('cls')
    print("Binary to Octal".center(150))
    enter_1=str(input("Enter the binay number(1 or 0): "))
    decimal=int(enter_1,2)
    octal=oct(decimal)
    time.sleep(0.5)
    print(f"The octal number is: {octal[2:]}")

#Binary to Hexadecimal
def B_to_H():
    os.system('cls')
    print("Binary to Hexadecimal".center(150))
    enter_1=str(input("Enter the binary number (1 or 0): "))
    decimal=int(enter_1,2)
    hexadecimal=hex(decimal)
    time.sleep(0.5)
    print(f"The hexadecimal number is:{hexadecimal[2:]}")

#Decimal to Binary
def D_to_B():
    print("Decimal to Binary".center(150))
    os.system('cls')
    enter_1=int(input("Enter the decimal number (0 to 9): "))
    binary=bin(enter_1)
    time.sleep(0.5)
    print(f"The binary number is: {binary[2:]}")

#Decimal to Octal
def D_to_O():
    os.system('cls')
    print("Decimal to Octal".center(150))
    enter_1=int(input("Enter the decimal number (0 to 9): "))
    octal=oct(enter_1)
    time.sleep(0.5)
    print(f"The octal number is: {octal[2:]}")

#Decimal to Hexadecimal
def D_to_H():
    os.system('cls')
    print("Decimal to Hexadecimal".center(150))
    enter_1=int(input("Enter the decimal number (0 to 9): "))
    hexadecimal=hex(enter_1)
    time.sleep(0.5)
    print(f"The hexadecimal number is: {hexadecimal[2:]}")

#Octal to Binary
def O_to_B():
    os.system('cls')
    print("Octal to Binary".center(150))
    enter_1=input("Enter the octal number (0 to 7): ")
    decimal=int(enter_1,8)
    binary=bin(decimal).replace("0b","")
    time.sleep(0.5)
    print(f"THe binary number is: {binary}")

#Octal to Decimal
def O_to_D():
    os.system('cls')
    print("Octal to Decimal".center(150))
    enter_1=input("Enter the octal number (0 to 7): ")
    decimal=int(enter_1,8)
    time.sleep(0.5)
    print(f"The decimal number is: {decimal}")

#Octal to Hexadecimal
def O_to_H():
    os.system('cls')
    print("Octal to Hexadecimal".center(150))
    enter_1=input("Enter the octal number (0 to 7): ")
    decimal=int(enter_1,8)
    hexadecimal=hex(decimal)
    time.sleep(0.5)
    print(f"The hexadecimal number is: {hexadecimal[2:]}")

#Hexadecimal to binary
def H_to_B():
    os.system('cls')
    print("Hexadecimal to binary".center(150))
    enter_1=input("Enter the hexadecimal number (0 to 9) and (a to f): ")
    decimal=int(enter_1,16)
    binary=bin(decimal)
    time.sleep(0.5)
    print (f"The binary number is: {binary[2:]}")

#Hexadecimal to decimal
def H_to_D():
    os.sys('cls')
    print("Hexadecimal to decimal".center(150))
    enter_1=input("Enter the hexadecimal number (0 to 9) and (a to f): ")
    decimal=int(enter_1,16)
    time.sleep(0.5)
    print(f"The decimal number is: {decimal}")

#Hexadecimal to Octal
def H_to_O():
    os.system('cls')
    print("Hexadecimal to Octal".center(150))
    enter_1=input("Enter the hexadecimal number (0 to 9) and (a to f): ")
    decimal=int(enter_1,16)
    octal=oct(decimal)
    print(f"The octal number is: {octal[2:]}")

def else_case():
    time.sleep(1)
    print("Invailed choice")
    enter_2=input("Do you want restart the program (Y/N): ")
    if enter_2=="Y" or enter_2=="y":
        choice()
    else:
        pass

if __name__=="__main__":
    start()
    choice()