def add(frist,second):
    addtion=frist+second
    print(f"{frist} + {second} = {addtion}".center(30))

def sub(frist,second):
    subtract=frist-second
    print(f"{frist} - {second} = {subtract}".center(30))

def muti(frist,second):
    multiply=frist*second
    print(f"{frist} X {second} = {multiply}".center(30))

def divide(frist,second):
    division=frist/second
    if second==0:
        print("Can not divided by zero")
    else:
        print(f"{frist} / {second} = {division}".center(30))

while True:
    frist=int(input("Enter the frist number "))
    second=int(input("Entert the second number "))
    operator=str(input("Enter the oprator(+,-,*,/) "))
    if operator=="+":
        add(frist,second)
    elif operator=="-":
        sub(frist,second)
    elif operator=="*":
        muti(frist,second)
    elif operator=="/":
        divide(frist,second)
    else:
        print("Invaild operator")
    Y_N=input("You to want to stop the program(Y/N) ")
    up=Y_N.upper()
    if up=="Y":
        break
    else:
        pass