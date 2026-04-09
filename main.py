
import time
import os


def main():
    print("1.Nepali Calendar")
    print("2.Alram")
    print("3.Calculator")
    print("4.Math test")
    print("5.Number guesser")
    print("6.Multification table")
    print("7.Rock paper sicissor")
    print("8.Password generator")
    print("9.Tempratuer convertor")
    print ("10.Number system")
    print()
    enter=int(input("Enter your choice: "))
    if enter==1:
        time.sleep(1)
        os.system('cls')
        import Nepali_calendar
    elif enter==2:
        time.sleep(1)
        os.system('cls')
        import Alram
    elif enter==3:
        time.sleep(1)
        os.system('cls')
        import calculate
    elif enter==4:
        time.sleep(1)
        os.system('cls')
        import math_test
    elif enter==5:
        time.sleep(1)
        os.system('cls')
        import numerguess
    elif enter==6:
        time.sleep(1)
        os.system('cls')
        import Multification
    elif enter==7:
        time.sleep(1)
        os.system('cls')
        import rock_paper_sicissors
    elif enter==8:
        time.sleep(1)
        os.system('cls')
        import password_genrator
    elif enter==9:
        time.sleep(1)
        os.system('cls')
        import Tempreture_convertor
    elif enter==10:
        time.sleep(1)
        os.system('cls')
        import Number_system
    else:
        time.sleep(1)
        print("Invalid choice")

if __name__=="__main__":
    while True:
        main()