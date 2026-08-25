# ==================== WELCOME ====================

import functions
from plaayer import Player
from time import sleep
import shutil
import momroom
import oth


def starting(player):
    functions.clear_screen()

    print(
        "\n====================WELCOME TO JOURNEY OF RUMORS=============================="
    )

    starting_text = [
        "You seem to be pretty confused arent you?",
        "I heard some rumors about you fs",
        "I have prepared some delicacies for you.",
        "",
        "What the f*** is even happening ffs",
        "Ughh such a stressful day, lemme pop one real quick hehe",
        "Shiii this some good shi right here"
    ]

    functions.sleeper(starting_text)

    while True:
        poping = input(
            "1. Pop one\n"
            "Enter your choice: "
        )

        if poping == "1":
            break
        else:
            print("Invalid input. Please enter '1' to pop one.")

    starting_text2 = [
        "You roll up a joint and light it up, the smoke fills your lungs and you feel a sense of euphoria wash over you.",
        "You take a deep inhale and exhale slowly, feeling the tension in your body melt away.",
        "As you continue to smoke, you feel your mind start to wander and your thoughts become more abstract.",
        "......",
        "......"
    ]

    functions.sleeper(starting_text2)

    functions.clear_screen()

    player.pop_substance(craving_change=-5)


def menu1(player):
    while True:
        functions.sleeper(
            ["Please select an option:", "1. START", "2. EXIT"],
            delay=0.04
        )

        choice = input("Enter your choice: ")

        if choice == "1":
            functions.sleeper(["Starting the game..."], delay=0.5)
            sleep(1)
            return

        if choice == "2":
            functions.sleeper(["Exiting the game..."], delay=0.5)
            sleep(1)
            raise SystemExit

        print("Invalid choice, please try again.")


def opening():
    functions.sleeper([
        "DAMN ARE YOU SURE WE SHOULD DO ####?, ITS LIT THE HARDEST SUBSTANCE IN THE WORLD",
        "BLEH, P****, YOU SCARED OR SOMETHING",
        "SYBAU, SURE SURE CMON",
        "......20 minutes later......",
        "HOLY SHI THIS HITS, I AM LIT SEEING STARS RN DAMN",
        "TOLD YA F*****",
        "ANYWAY DONT TELL ANYONE ABOUT IT",
        "OFC LMAO",
        "SHI BRO I DON'T THINK I CAN KEEP MY EYES OPEN ANYMORE",
        "UGHHH SHI F*** F*** F***"
    ])

    functions.sleeper([
        "U hear voices inside of you",
        "..........",
        "U LOVE SUBSTANCES, I CAN TELL",
        "I CAN TELL YOU LIKE IT, I CAN TELL YOU LIKE IT",
        "THE RUMORS SURELY ARE WORTHY",
        "I CAN TELL YOU LIKE IT, I CAN TELL YOU LIKE IT"
    ])


def check_player_status(player):
    if player.health <= 0:
        functions.death()
        return True
    elif player.craving >= 100:
        functions.rehab()
        return True
    elif player.craving <= 0:
        functions.win()
        return True
    return False


def game_loop(player):
    while True:
        functions.clear_screen()

        width = shutil.get_terminal_size().columns
        print(f"\033[1;{width - 25}HHEALTH: {player.health}%")
        print(f"\033[2;{width - 25}HCRAVING: {player.craving}%")

        print("\nChoose your next action:")
        print("1. Pop another one")
        print("2. Go out of your room")

        input_choice = input("Enter your choice: ")

        if input_choice == "1":
            functions.clear_screen()
            functions.sleeper([
                "You roll up a joint and light it up, the smoke fills your lungs"
            ])
            functions.clear_screen()

            player.pop_substance(craving_change=-5)

            # Check status after popping
            if check_player_status(player):
                return

            sleep(1)

        elif input_choice == "2":
            functions.clear_screen()
            functions.sleeper([
                "You decide to go out of your room"
            ])
            return

        else:
            print("Invalid choice, please try again.")
            sleep(1)


def choose_location():
    functions.clear_screen()

    print("Choose your destination:")
    print("1. Mom's room")
    print("2. Outside the house")

    while True:
        outside_mom = input("Enter your choice: ")

        if outside_mom in ("1", "2"):
            return outside_mom

        print("Enter a valid choice")


def main():
    opening()

    player = Player()

    menu1(player)

    starting(player)

    # Check status after starting (intro pop)
    if check_player_status(player):
        return

    game_loop(player)

    # Check status after game loop
    if check_player_status(player):
        return

    location = choose_location()

    if location == "1":
        momroom.mom_room(player)
    elif location == "2":
        oth.going_out(player)

    # Final check
    if check_player_status(player):
        return


if __name__ == "__main__":
    main()