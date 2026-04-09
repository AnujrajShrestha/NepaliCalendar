import sys
import time
from time import sleep
from colorama import Fore,Style,init,Back

init(autoreset=True)

def print_lyrics():
    lines = [
        ("Secrets I have held in my heart",0.09),
        ("Are harder to hide than I thought",0.07),
        ("Maybe I just wanna be yours",0.1),
        ("I wanna be yours",0.07),
        ("Wanna be yourssss",0.15),
        ("Wanna be yourssss",0.15),
        ("Wanna be yourssss",0.15),
        ("Wanna be yourssss",0.15),
    ]

    delays = [0.9, 0.9, 0.6, 0.8, 0.8,0.8,0.8,0.6]
    
    print(f'🎧 Now playing - "I wanna be yours" - Arctic Monkeys\n')
    sleep(1)

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(Fore.CYAN + char,end="")
            sys.stdout.flush() 
            sleep(char_delay)
        print("")
        time.sleep(delays[i])

print_lyrics()
