import time

def c_to_f():
    celsius=int(input("Enter the temperature on celsius "))
    fahrenheit=(celsius*9/5)+32
    time.sleep(1)
    print(f"The temperature in fahrenheit is: {fahrenheit}")

def f_to_c():
    fahrenheit=int(input("Enter the temperature to fehrenheit "))
    celsius=(fahrenheit-32)*5/9
    time.sleep(1)
    print(f"The temoerature is: {celsius}")

def c_to_k():
    celsius=int(input("Enter the tempreature to celsius "))
    kelvin=celsius+273
    time.sleep(1)
    print(f"The tempreature in kelvin is: {kelvin}")

def k_to_c():
    kelvin=int(input("Enter the tempreature in kelvin "))
    celsius=kelvin-273
    time.sleep(1)
    print(f"The tempreature in celsius is: {celsius}")

def input_1():
    time.sleep(1)
    print("1.Celsius to Fahrenheit conversion")
    print("2.Fahrenheit to celsius conversion")
    print("3. Celsius to kelvin conversion")
    print("4.Kelvin to celsius conversion")
    time.sleep(1)
    enter=int(input("Enter your choice "))
    if enter==1:
        c_to_f()
    elif enter==2:
        f_to_c()
    elif enter==3:
        c_to_k()
    elif enter==4:
        k_to_c()
    else:
        print("Invaild choice")
        

if __name__=="__main__":
    input_1()