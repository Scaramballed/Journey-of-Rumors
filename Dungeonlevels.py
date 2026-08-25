import functions
import random
import time
import studying
import oth


def start_window_dungeon(player, show_intro=True):
    """Show the dungeon level menu and return when the player leaves it."""

    if show_intro:
        functions.sleeper([
            "HIII I AM ZIGGLY",
            "The manager of the dungeon",
            "hehehe are you familiar with me?",
            "anyway go ahead and crush this dungeon",
            "CIAOO"
        ])

    functions.clear_screen()

    functions.sleeper([
        "CHOOSE YOUR LEVELS",
        "1. dumbahh get a job",
        "2. ???",
        "3. ???",
        "4. Leave the dungeon"
    ])

    while True:
        level = input("Enter your choice cutie: ")

        if level == "1":
            levelone(player)

        elif level == "4":
            functions.sleeper(["You leave the dungeon and return to Mom's Room."])
            return

        else:
            print("Choose a valid choice vro ughhh u make me sick")


def levelone(player):
    a = random.randint(10, 500)
    b = random.randint(10, 500)

    correct_answer = a + b

    start = time.time()

    try:
        answer = int(input(f"What is {a} + {b}? "))
    except ValueError:
        print("Invalid input. You lose.")
        player.change_craving(amount=20)
        return

    elapsed = time.time() - start

    if elapsed > 20:
        print("TIME'S UP")
        player.change_craving(amount=20)

    elif answer == correct_answer:
        functions.sleeper(["CORRECT",
              "WITH THIS YOU HAVE UNLOCKED A NEW ACTIVITY",
              "NOW YOU CAN STUDY "
              "(decreases your cravings but be careful too much studying is hella stressful)",
              ])

        functions.sleeper(["Choose your next action:",
                           "1. Go to studying session",
                           "2. Go outside"])
        
        while True:
            choice = input("Enter your choice: ")
            
            if choice == "1":
                result = studying.session(player)
                if result == "outside":
                    return
                break
                
            elif choice == "2":
                oth.going_out(player)
                return
                
            else:
                print("Choose a valid option dumbahh")

    else:
        print("WRONG")
        player.change_craving(amount=20)


def leveltwo(player):
    functions.sleeper(["under construction twh sadly"])