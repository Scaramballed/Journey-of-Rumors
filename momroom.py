import functions
import Dungeonlevels
import oth


def entering_the_dungeon(player):
    Dungeonlevels.start_window_dungeon(player)


def mom_room(player):
    functions.clear_screen()

    functions.sleeper([
        "BREH MOM WILL FS K*** ME IF SHE FINDS OUT I WAS SMOKING",
        "IG ITS AIGHT ATP WHO EVEN DOESN'T KNOW",
        "GOAT FOR A REASON BAHAHAHHAHA",
        ".........",
        ".........",
        "Your mom doesn't say anything but the moment you come in your mom goes outside",
        "You feel offended",
        "......",
        "......"
    ])

    functions.sleeper([
        "Choose your next action:",
        "1. Move around",
        "2. Scream at your mom"
    ])

    while True:
        mom_room_choice = input("Enter your choice: ")

        if mom_room_choice == "2":
            functions.sleeper([
                "Your mom ignores you cause at the end of the day",
                "you infact still are a bum lmao",
                "Get a life man"
            ])
            player.pop_substance(craving_change=10)
            break

        elif mom_room_choice == "1":
            functions.sleeper([
                "You move around as if you are mindlessly searching for something"
            ])
            break

        else:
            functions.sleeper([
                "Choose a valid choice FUCKASS"
            ])

    functions.sleeper([
        "You find a key",
        "You smile a little and think of all the money you could get to buy more substance",
        "You pathetic loser",
        "....",
        "Anyway, the moment you pick up the key, your mom's room changes",
        "......",
        "......",
        "......",
        "You hear a mysterious voice",
        "%^^&F#QAF#$",
        "##$$$^&@@",
        "Welc###",
        "WELCOME TO THE DUNGEON OF RUMORS",
        "Here you can experience a little hint of ####",
        "There are multiple levels you could progress through",
        "ENJOY!!!"
    ])

    entering_the_dungeon(player)
    mom_room_menu(player)


def mom_room_menu(player):
    while True:
        functions.clear_screen()

        functions.sleeper([
            "You are back in Mom's Room.",
            "Choose your next action:",
            "1. Enter the Dungeon of Rumors",
            "2. Go outside"
        ])

        choice = input("Enter your choice: ")

        if choice == "1":
            Dungeonlevels.start_window_dungeon(player, show_intro=False)

        elif choice == "2":
            oth.going_out(player)
            return

        else:
            print("Choose a valid choice FUCKASS")