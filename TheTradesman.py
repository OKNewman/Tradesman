from os import system, name
from time import sleep
from TitleCards import companycard
from TitleCards import gametitle
# import winsound

bool_exit = False

#Initializing variables
playername = ""
player_asset_widget = 0
player_asset_app = 0
player_asset_stock = 0
player_asset_dosh = 10000
player_day = 1
player_location = "coffee_shop"
loc_price_widget = 10
loc_price_app = 50
loc_price_stock = 100


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


def new_game():
    print("\n" * 10)
    print("==Welcome, Tradesman==")
    print("\n" * 5)
    playername = input("What is your name?: ")  # Get input for user name
    clear()
    sleep(1)
    print("\n" * 10)
    print("Welcome, " + playername + ".")   # TODO: Move this to whenever you start playing, even when loading
    return playername


def travel_menu():
    print("==========TRAVEL MENU==========")
    print("Coming soon!")
    sleep(1)    
    return


def buy_action(asset, asset_price):
    global player_asset_dosh
    clear()
    status_commerce()
    str_amount_asset = input("Buying how many?: ")
    amount_asset = int(str_amount_asset)
    dosh_diff = amount_asset * asset_price
    player_asset_dosh = player_asset_dosh - dosh_diff
    asset = asset + amount_asset
    print("Gaining " + str(amount_asset) + " for " + str(dosh_diff) + " dosh.")
    return asset


def sell_action(asset, asset_price):
    global player_asset_dosh
    clear()
    status_commerce()
    str_amount_asset = input("Selling how many?: ")
    amount_asset = int(str_amount_asset)
    dosh_diff = amount_asset * asset_price
    player_asset_dosh = player_asset_dosh + dosh_diff
    asset = asset - amount_asset
    print("Gaining " + str(dosh_diff) + " dosh for " + str(amount_asset) + " unit(s).")
    return asset


def buy_menu():
    global player_asset_widget
    global player_asset_app
    global player_asset_stock
    print("==========BUY MENU==========")
    status_commerce()
    print("1. Widget(s)")
    print("2. App(s)")
    print("3. Stock")
    print("4. Back to Main Menu")
    choice = input("What're ya buyin'?: ")
    if choice == "1":
        print("Widgets, eh?")
        player_asset_widget = buy_action(player_asset_widget, loc_price_widget)
        return
        #TODO: Add purchase validation
    if choice == "2":
        print("Apps, huh?")
        player_asset_app = buy_action(player_asset_app, loc_price_app)
        return
    if choice == "3":
        print("High roller wants some stock?")
        player_asset_stock = buy_action(player_asset_stock, loc_price_stock)
        return
    if choice == "4":
        clear()
        game_menu()
    else:
        print("Choice invalid. Try again.")
        sleep(1)
        clear()
        buy_menu()
        # TODO: add an else here to catch invalid answers
        # Note: It seems to work anyway


def sell_menu():
    global player_asset_widget
    global player_asset_app
    global player_asset_stock
    print("==========SELL MENU==========")
    status_commerce()
    print("1. Widget(s)")
    print("2. App(s)")
    print("3. Stock")
    print("4. Back to Main Menu")
    choice = input("What're ya sellin'?: ")
    if choice == "1":
        print("Widgets, eh?")
        player_asset_widget = sell_action(player_asset_widget, loc_price_widget)
        return
        #TODO: Add purchase validation
    if choice == "2":
        print("Apps, huh?")
        player_asset_app = sell_action(player_asset_app, loc_price_app)
        return
    if choice == "3":
        print("Cashing out some stock?")
        player_asset_stock = sell_action(player_asset_stock, loc_price_stock)
        return
    if choice == "4":
        clear()
        game_menu()
    else:
        print("Choice invalid. Try again.")
        sleep(1)
        clear()
        buy_menu()
        # TODO: add an else here to catch invalid answers
        # Note: It seems to work anyway


def main_menu():
    print("Menu select kinda works?")
    sleep(2)
    clear()
    game_menu()
    return


def status_commerce():
    print("You are: " + playername + (" " * 10) + "|Dosh: " + str(player_asset_dosh) + (" " * 10) + "|Day: " + str(player_day))
    print("        ------Inventory------|-------Prices------")
    print("Widgets: " + str(player_asset_widget) + "         |       " + str(loc_price_widget))
    print("Apps:    " + str(player_asset_app) + "         |       " + str(loc_price_app))
    print("Stock:   " + str(player_asset_stock) + "         |       " + str(loc_price_stock))
    print("\n" * 4)


def game_menu_select():
    print("1. Buy")
    print("2. Sell")
    print("3. Travel")
    print("4. Exit")
    choice = input("Make a selection: ")
    if choice == "1":
        clear()
        buy_menu()
        sleep(1)
    if choice == "2":
        clear()
        sell_menu()
    if choice == "3":
        clear()
        travel_menu()
    if choice == "4":
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
        # Note: It seems to work anyway
    return


def save_game():
    print("Save option coming soon!")
    # Do I want to autosave?
    return


def load_game():
    print("Load option coming soon!")
    return


def exit_game():
    print("See you next time, " + playername + "!")
    save_game()
    sleep(2)
    clear()
    exit()


def game_menu():
    print("==========Main Menu==========")
    status_commerce()
    game_menu_select()
    return


# winsound.PlaySound("ADG_3DO.wav", winsound.SND_ASYNC)   # Research OS agnostic sound solution


clear()

startup()
load_game()
playername = new_game()

while not bool_exit:
    game_menu()