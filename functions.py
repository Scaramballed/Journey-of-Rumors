from time import sleep
import shutil

def sleeper(text, delay=0.04):
    for line in text:
        for character in line:
            print(character, end="", flush=True)
            sleep(delay)
        print()
        sleep(1)

def clear_screen():
    print("\033[3J\033[2J\033[H", end="", flush=True)

def pop_one(player):
    """Handle the act of popping one substance."""
    clear_screen()
    sleeper([
        "You roll up a joint and light it up,",
        "the smoke fills your lungs."
    ])
    clear_screen()
    player.pop_substance(craving_change=-10)
    
    # After popping, ask what to do next
    return after_pop_choice(player)

def after_pop_choice(player):
    """Ask player what to do after popping."""
    sleeper([
        "You're feeling a bit better.",
        "What do you want to do now?"
    ])
    
    while True:
        sleeper([
            "1. Go back to the dungeon",
            "2. Go outside"
        ])
        choice = input("Enter your choice: ")
        
        if choice == "1":
            sleeper(["You head back to the dungeon."])
            return "dungeon"
            
        elif choice == "2":
            import oth
            oth.going_out(player)
            return "outside"
            
        else:
            print("Choose a valid option")

def death():
    clear_screen()
    sleeper([
        "Welp...",
        "you died bro bleh"
    ])
    exit()

def rehab():
    clear_screen()
    sleeper([
        "BROOO LMAOOO",
        "IMAGINE DOING TOO MUCH SUBSTANCE",
        "GO AND ROT IN REHAB BRO ABAHAHAHBAHB"
    ])
    exit()

def win():
    clear_screen()
    sleeper([
        "BROO WTHHH YOU ACTUALLY DID ESCAPE FROM YOUR ADDICTION",
        "THATS LITERALLY LIKE SO F****** COOL",
        "I LWK WANNA GROW UP TO BE LIKE YOU",
        "ANYWAY LOLSIE I M UR CONCIOUSNESS",
        "GUESS WHO BROKE FREEE FROM HIS ADDICTIONS",
        "HOPE YOU WONT DO IT AGAIN F******"
    ])
    exit()