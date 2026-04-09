import time
import os
import datetime
from colorama import init,Style,Fore,Back
init(autoreset=True)

now=datetime.datetime.now()
months=int(now.strftime("%m"))
dates=int(now.strftime("%d"))

char="Nepali Calendar"
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

def hilight_color(date:str,c_date:int):
    if date == str(c_date):
        return Back.GREEN+Fore.WHITE+ (f" {date}")+ Style.RESET_ALL
    else:
        return Fore.RED + date + Style.RESET_ALL 
    

def hilight_date(date2:str,c_date2:int):
    if date2==str(c_date2):
        return Back.GREEN + Fore.WHITE +(f" {date2}")+Style.RESET_ALL
    else:
        return date2

def show_english_date():
    print(now.strftime(f"{20}%y-%m-%d").center(30))


def Baisakha(current_date):
    print ("Baiskha".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    Monday=["Mon",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    Tuesday=["Tue",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    wednesday=["Wed",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("31",current_date)]
    thursday=["Thu",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("5",current_date),hilight_date("12",current_date),hilight_date("19",current_date),
            hilight_date("26",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("6",current_date),hilight_color("13",current_date),
                hilight_color("20",current_date),hilight_color("27",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def jastha(current_date):
    print ("Jatsha".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("4",current_date),hilight_date("11",current_date),
            hilight_date("18",current_date),hilight_date("25",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("23",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    wednesday=["Wed",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    thursday=["Thu",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    friday=["Fri",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("3",current_date),hilight_color("10",current_date),
                hilight_color("17",current_date),hilight_color("24",current_date),hilight_color("31",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def Asar(current_date):
    print ("Asar".center(30))
    Sunday=["Sun",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    Monday=["mon",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    Tuesday=["Tue",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("31",current_date)]
    wednesday=["Wed",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("32",current_date)]
    thursday=["Thu",hilight_date("5",current_date),hilight_date("12",current_date),hilight_date("19",current_date),
            hilight_date("26",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("6",current_date),hilight_date("13",current_date),hilight_date("20",current_date),
            hilight_date("27",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("7",current_date),hilight_color("14",current_date),
                hilight_color("21",current_date),hilight_color("28",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def sauuna(current_date):
    print ("Sauuna".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("4",current_date),hilight_date("11",current_date),
            hilight_date("18",current_date),hilight_date("25",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("26",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    wednesday=["Wed",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    thursday=["Thu",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    friday=["Fri",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("3",current_date),hilight_color("10",current_date),
                hilight_color("17",current_date),hilight_color("24",current_date),hilight_color("31",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def vadauu(current_date):
    print ("Vadauu".center(30))
    Sunday=["Sun",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    Monday=["mon",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    Tuesday=["Tue",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("31",current_date)]
    wednesday=["Wed",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("-",current_date)]
    thursday=["Thu",hilight_date("5",current_date),hilight_date("12",current_date),hilight_date("19",current_date),
            hilight_date("26",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("6",current_date),hilight_date("13",current_date),hilight_date("20",current_date),
            hilight_date("27",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("7",current_date),hilight_color("14",current_date),
                hilight_color("21",current_date),hilight_color("28",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3)) 

def asoj(current_date):
    print ("Asoj".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("26",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    wednesday=["Wed",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    thursday=["Thu",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    friday=["Fri",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("31",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("4",current_date),hilight_color("11",current_date),
            hilight_color("18",current_date),hilight_color("25",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
                thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def karti(current_date):
    print ("Kartik".center(30))
    Sunday=["Sun",hilight_date("30",current_date),hilight_date("2",current_date),hilight_date("9",current_date),
            hilight_date("16",current_date),hilight_date("23",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("3",current_date),hilight_date("10",current_date),
            hilight_date("17",current_date),hilight_date("24",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("4",current_date),hilight_date("11",current_date),
            hilight_date("18",current_date),hilight_date("25",current_date)]
    wednesday=["Wed",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("26",current_date)]
    thursday=["Thu",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    friday=["Fri",hilight_color("--",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("1",current_date),hilight_color("8",current_date),
            hilight_color("15",current_date),hilight_color("22",current_date),hilight_color("29",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def mansri(current_date):
    print ("Mansri".center(30)) 
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    Monday=["mon",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    Tuesday=["Tue",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("-",current_date)]
    wednesday=["Wed",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("-",current_date)]
    thursday=["Thu",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("5",current_date),hilight_date("12",current_date),hilight_date("19",current_date),
            hilight_date("26",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("6",current_date),hilight_color("13",current_date),
            hilight_color("20",current_date),hilight_color("27",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def push(current_date):
    print ("Push".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    Tuesday=["Tue",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("30",current_date)]
    wednesday=["Wed",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("-",current_date)]
    thursday=["Thu",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("5",current_date),hilight_color("12",current_date),
            hilight_color("19",current_date),hilight_color("26",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def madh(current_date):
    print ("Madh".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("4",current_date),hilight_date("11",current_date),
            hilight_date("18",current_date),hilight_date("25",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("26",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    wednesday=["Wed",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    thursday=["Thu",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    friday=["Fri",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("3",current_date),hilight_color("10",current_date),
                hilight_color("17",current_date),hilight_color("24",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def falgun(current_date):
    print("Faglun".center(30))
    Sunday=["Sun",hilight_date("-",current_date),hilight_date("3",current_date),hilight_date("10",current_date),
            hilight_date("17",current_date),hilight_date("24",current_date)]
    Monday=["mon",hilight_date("-",current_date),hilight_date("4",current_date),hilight_date("11",current_date),
            hilight_date("18",current_date),hilight_date("25",current_date)]
    Tuesday=["Tue",hilight_date("-",current_date),hilight_date("5",current_date),hilight_date("12",current_date),
            hilight_date("19",current_date),hilight_date("26",current_date)]
    wednesday=["Wed",hilight_date("-",current_date),hilight_date("6",current_date),hilight_date("13",current_date),
            hilight_date("20",current_date),hilight_date("27",current_date)]
    thursday=["Thu",hilight_date("-",current_date),hilight_date("7",current_date),hilight_date("14",current_date),
            hilight_date("21",current_date),hilight_date("28",current_date)]
    friday=["Fri",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("2",current_date),hilight_color("9",current_date),
                hilight_color("16",current_date),hilight_color("23",current_date),hilight_color("30",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def chitra(current_date):
    print("Chitra".center(30))
    Sunday=["Sun",hilight_date("1",current_date),hilight_date("8",current_date),hilight_date("15",current_date),
            hilight_date("22",current_date),hilight_date("29",current_date)]
    Monday=["mon",hilight_date("2",current_date),hilight_date("9",current_date),hilight_date("16",current_date),
            hilight_date("23",current_date),hilight_date("30",current_date)]
    Tuesday=["Tue",hilight_date("3",current_date),hilight_date("10",current_date),hilight_date("17",current_date),
            hilight_date("24",current_date),hilight_date("-",current_date)]
    wednesday=["Wed",hilight_date("4",current_date),hilight_date("11",current_date),hilight_date("18",current_date),
            hilight_date("25",current_date),hilight_date("-",current_date)]
    thursday=["Thu",hilight_date("5",current_date),hilight_date("12",current_date),hilight_date("19",current_date),
            hilight_date("26",current_date),hilight_date("-",current_date)]
    friday=["Fri",hilight_date("6",current_date),hilight_date("13",current_date),hilight_date("20",current_date),
            hilight_date("27",current_date),hilight_date("-",current_date)]
    saturday=[hilight_color("Sat",current_date),hilight_color("7",current_date),hilight_color("14",current_date),
                hilight_color("21",current_date),hilight_color("28",current_date),hilight_color("-",current_date)]
    for calendar in range(0,6,1):
        print (Sunday[calendar].center(3),Monday[calendar].center(3),Tuesday[calendar].center(3),wednesday[calendar].center(3),
            thursday[calendar].center(3),friday[calendar].center(3),saturday[calendar].center(3))

def convert_date(a,b,c,d,m,d1,d2,month):
    Nepali_date=d1
    for loops in range(a,b,1):
        if dates==loops:
            print (f"2082-{month}-{Nepali_date}".center(30))
            return Nepali_date
        Nepali_date+=1
    if months==m:
        Nepali_date=d2
        for loops in range(c,d,1):
            if dates==loops:
                print (f"2082-{month}-{Nepali_date}".center(30))
                return Nepali_date
            Nepali_date+=1
    print("Current momth".center(30))

print('''
    1.Show current date
    2.Show all the months
    3.Show the entered month''')
time.sleep(1)
enter=int(input("Enter your choice(1 to 3): "))
if enter==1:
    pass
elif(enter==2):
    current_date=40
    Baisakha(current_date)
    jastha(current_date)
    Asar(current_date)
    sauuna(current_date)
    vadauu(current_date)
    asoj(current_date)
    karti(current_date)
    mansri(current_date)
    push(current_date)
    madh(current_date)
    falgun(current_date)
    chitra(current_date)
elif(enter==3):
    current_date=40
    enter2=int(input("Enter the month (1 to 12): "))
    if (enter2==1):
        Baisakha(current_date)
    elif(enter2==2):
        jastha(current_date)
    elif(enter2==3):
        Asar(current_date)
    elif(enter2==4):
        sauuna(current_date)
    elif(enter2==5):
        vadauu(current_date)
    elif(enter2==6):
        asoj(current_date)
    elif(enter2==7):
        karti(current_date)
    elif(enter2==8):
        mansri(current_date)
    elif(enter2==9):
        push(current_date)
    elif(enter2==10):
        madh(current_date)
    elif(enter2==11):
        falgun(current_date)
    elif(enter2==12):
        chitra(current_date)
    else:
        print("Invalid choice")
else:
    print("Invalid choice")

if (months==1 and dates>=15 and dates<=31) or (months==2 and dates>=1 and dates<=12):
    show_english_date()
    nep_date=convert_date(15,31,1,12,2,1,18,10)
    madh(nep_date)
elif (months==2 and dates>=13 and dates<=28) or (months==3 and dates>=1 and dates<=14):
    show_english_date()
    nep_date=convert_date(13,28,1,14,3,1,17,11)
    falgun(nep_date)
elif (months==3 and dates>=15 and dates<=31) or (months==4 and dates>=1 and dates<=13):
    show_english_date()
    nep_date=convert_date(15,31,1,13,4,1,18,12)
    chitra(nep_date)
elif (months==4 and dates>=14 and dates<=30) or (months==5 and dates>=1 and dates<=14):
    show_english_date()
    nep_date=convert_date(14,30,1,14,5,1,18,1)
    Baisakha(nep_date)
elif (months==5 and dates>=15 and dates<=31) or (months==6 and dates>=1 and dates<=14):
    show_english_date()
    nep_date=convert_date(15,31,1,14,6,1,18,2)
    jastha(nep_date)
elif (months==6 and dates>=15 and dates<=30) or (months==7 and dates>=1 and dates<=16):
    show_english_date()
    nep_date=convert_date(15,30,1,16,7,1,17,3)
    Asar(nep_date)
elif (months==7 and dates>=17 and dates<=31) or (months==8 and dates>=1 and dates<=16):
    show_english_date()
    nep_date=convert_date(17,31,1,16,8,1,16,4)
    sauuna(nep_date)
elif (months==8 and dates>=17 and dates<=31) or (months==9 and dates>=1 and dates<=16):
    show_english_date()
    nep_date=convert_date(17,31,1,16,9,1,16,5)
    vadauu(nep_date)
elif (months==9 and dates>=17 and dates<=30) or (months==10 and dates>=1 and dates<=17):
    show_english_date()
    nep_date=convert_date(17,30,1,17,10,1,15,6)
    asoj(nep_date)
elif (months==10 and dates>=18 and dates<=31) or (months==11 and dates>=1 and dates<=16):
    show_english_date()
    nep_date=convert_date(18,31,1,16,11,1,16,7)
    karti(nep_date)
elif (months==11 and dates>=17 and dates<=30) or (months==12 and dates>=1 and dates<=15):
    show_english_date()
    nep_date=convert_date(17,30,1,15,12,1,15,8)
    mansri(nep_date)
elif (months==12 and dates>=16 and dates<=31) or (months==1 and dates>=1 and dates<=14):
    show_english_date()
    nep_date=convert_date(16,31,1,14,1,1,17,9)
    push(nep_date)