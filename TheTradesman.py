from os import system, name
from time import sleep
from TitleCards import titlescreen


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# 80x24 is the common dimension for a terminal; spot 25 prints on the next line below? Read up on this
# create better "print" function (self-scaling lines/frames with piping), store in separate python file


clear()

titlescreen()
sleep()
clear()

print("==Welcome, Tradesman==")

sleep(2)
clear()
playername = input("What is your name?")     # Get input for user name
