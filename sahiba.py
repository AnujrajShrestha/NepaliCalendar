import sys
import time
from time import sleep

Red="\033[91m"
Reset="\033[0m"

def print_lyrics():
    lines = [
        
        ("Baato-baato mein hi, khwabo-khwabo mein hi mere qareeb hai tu",0.06),
        ("Teri talab mujhko, teri talab, jaana, ho to khahi rubaroo",0.07),
        ("Shor-sharaaba ho seene mein hai mere kaise bayaan main karoon?",0.07),
        ("Haal jo mera hai main kis ko battaun?",0.09),
        ("Mere sahiba dil na kairaaye ka thoda toh sambhaalo naa",0.12),
        ("Nazuk hai yeh toot jaatta hai",0.07)
    ]

    delays = [0.9, 0.7, 0.8, 0.6, 0.6,0.7]
    
    print("🎧 Now playing - Sahiba❤️\n")
    sleep(1)

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"{Red}{char}{Reset}", end="")
            sys.stdout.flush()
            sleep(char_delay)
        print("")
        time.sleep(delays[i])

print_lyrics()
