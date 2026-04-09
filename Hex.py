import sys
from time import sleep
import time

def print_lyrics():
    lines=[
        ("East and west, I'm rackin' up all my bread uh",0.04),
        ("Power on me, I'm feelin' just like a Tesla",0.04),
        ("Too much tree,the smoke is makin' my chest hurt",0.04),
        ("Girl on me, I'm thinking I should her",0.03),
        ("Ayy, I'm tinkling I should arrest",0.03),
        ("All night long, she puttin' me to the test",0.04),
        ("Got a lot on, I'm tryna take off the rest",0.04),
        ("Cleaning up my lines, I say nothin' but the best",0.04),
        ("Hey girl, you're the cutest that I see",0.04),
        ("So brigth, I'm not using my visine",0.03),
    ]
    for i,(lines,char_delays) in enumerate(lines):
        for char in lines:
            print (char,end="")
            sys.stdout.flush()
            sleep(char_delays)
        print('')
        
print_lyrics()