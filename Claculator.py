while True:
    frist=int(input("Enter the first number "))
    second=int(input("Enter the second number "))
    oprator=str(input("Enter your oprator(+,-,*,/) "))
    if oprator=="+":
        add=frist+second
        print(frist,"+",second,"=",add)
    elif oprator=="-":
        sub=frist-second
        print(frist,"-",second,"=",sub)
    elif oprator=="*":
        multiply=frist*second
        print(frist,"*",second,"=",multiply)
    elif oprator=="/":
        divide=frist/second
        print(frist,"/",second,"=",divide)
    else:
        print("Invaild opration")