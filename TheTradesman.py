from os import system, name
from time import sleep
from TitleCards import companycard
from TitleCards import gametitle
import winsound

bool_exit = False

#Initializing variables
playername = ""
player_asset_widget = 0
player_asset_app = 0
player_asset_stock = 0
player_asset_dosh = 0
player_day = 0
player_location = ""

def default_vars():
    player_asset_widget = 0
    player_asset_app = 0
    player_asset_stock = 0
    player_asset_dosh = 10000
    player_day = 1
    player_location = "coffee_shop"
    return


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# 80x24 is the common dimension for a terminal; spot 25 prints on the next line below? Read up on this
# create better "print" function (self-scaling lines/frames with piping), store in separate python file

def startup():
    companycard()
    sleep(1)
    clear()
    sleep(1)
    gametitle()
    sleep(3)
    clear()
    return


def save_data_check():
    print("save data check coming soon!")
    return

def new_game():
    print("\n" * 10)
    print("==Welcome, Tradesman==")
    print("\n" * 5)
    playername = input("What is your name?")  # Get input for user name
    clear()
    sleep(1)
    print("\n" * 10)
    default_vars()
    print("Welcome, " + playername + ".")   # TODO: Move this to whenever you start playing, even when loading
    return


def main_menu():
    print("Menu select kinda works?")
    sleep(2)
    clear()
    game_menu()
    return


def game_menu_select():
    choice = input("Make a selection: ")
    if choice == "1":
        clear()
        print("Are you sure you want to exit The Tradesman?")
        print("1. Yes")
        print("2. No")
        confirm = input("Make a selection: ")
        if confirm == "1":
            exit_game()
        if confirm == "2":
            clear()
            game_menu()
        # TODO: add an else here to catch invalid answers
    return


def save_game():
    print("Save option coming soon!")
    # Do I want to autosave?
    return


def load_game():
    print("Load option coming soon!")
    return


def exit_game():
    exit()


def game_menu():
    print("==========CHOOSE AN OPTION==========")
    print("1. Exit")
    game_menu_select()
    return


winsound.PlaySound("ADG_3DO.wav", winsound.SND_ASYNC)   # Research OS agnostic sound solution


clear()

startup()
save_data_check()
new_game()

while not bool_exit:
    game_menu()

print("See you next time, " + playername + "!")
sleep(2)
clear()