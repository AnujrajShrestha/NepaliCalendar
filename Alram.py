import time as ti
import os
import winsound

time=ti.strftime('%H:%M:%S')
print(time.center(55))
hour=int(input("Enter hours: "))
minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))
ti.sleep(2)
os.system('cls')
ti.sleep(1)
while True:
    for Alarm in range(1234):
        print (f"{hour}:{minutes}:{seconds}".center(55),end='')
        print(ti.strftime('%H:%M:%S').center(10),end='')
        ti.sleep(0.3)
        os.system('cls')
        C_hour=int(ti.strftime('%H'))
        C_minutes=int(ti.strftime('%M'))
        C_seconds=int(ti.strftime('%S'))
        if hour<=C_hour and minutes<=C_minutes and seconds<=C_seconds:
            print ("Its time to wake up".center(55))
            for sound in range(1,11):
                winsound.Beep(840,1200)
            break
    break





