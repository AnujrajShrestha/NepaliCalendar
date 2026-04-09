import sys
from time import sleep
import time

def print_lyrics():
    lines=[
        ("Yeah",0.010),
        ("My hands steady",0.05),
        ("I feel ready",0.05),
        ("But my legs heavy",0.05),
        ("I don't get it ",0.05),
        ("How come I haave't hit it",0.05),
        ("Already, still working",0.05),
        ("I'm still learning",0.05),
        ("I'm still searching",0.05),
        ("Finally earning something",0.04),
        ("Finally turing something",0.04),
        ("Called a profit",0.03),
        ("If I hear you talkin'shit",0.05),
        ("Don't get caught in it",0.03),
        ("I'll be poppin' off and hit yo'ass",0.05),
        ("Yeah I promiss this",0.05),
        ("You ain't stopping this",0.05),
        ("Cross my shit",0.05),
        ("You'll be knocked unconscious bitch",0.05),
        ("That's the consequence",0.04),
        ("I got this",0.03),
        ("I will not quit",0.03),
        ("Man, I'm on it",0.04),
        ("Honest",0.08),
        ("I'm gon'launch quick",0.05),
        ("Then I'm gone",0.04),
        ("It's just a matter of time",0.05),
        ("Before I'm over the climb",0.05),
        ("And moving onto my prime",0.05),
        ("Just quit my nine to five",0.05),
        ("I'm rockin'",0.06),
        ("And they watching",0.05),
        ("'Cause it's shockin'",0.05),
        ("Droppin'",0.05),
        ("All these top ten",0.05),
        ("Song not stopping",0.05),
        ("It's time to live my life",0.05),
        ("It's time to live not die",0.04),
        ("Wish, I could slow down time",0.04),
        ("And just enjoy the climb",0.04)
    ]
    for i,(lines,char_delays) in enumerate(lines):
        for char in lines:
            print (char,end="")
            sys.stdout.flush()
            sleep(char_delays)
            time.sleep(0.01)
        print('')
print_lyrics()