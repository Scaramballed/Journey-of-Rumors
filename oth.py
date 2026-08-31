import functions
import time


def going_out(player):
    functions.sleeper([
        "You go outside banging the door loud asl",
        "Your mom screams at you as usual",
        "Hey welcome to the outside world",
        "As for now we are only physically able to go to few places, fuckass addict",
        "so fucking weak"
    ])

    functions.clear_screen()

    functions.sleeper([
        "Where do u wanna go cutie:",
        "1. Craving lake",
        "2. Go running"
    ])

    choice_oth = input("Enter your choice: ")

    if choice_oth == "1":
        functions.sleeper([
            "ITS PRETTY FAR VRO YOU HAVE YOU RUN EITHER WAYS",
            "ABHABAHBAHBAHBA",
            "ANYWAY GET READY FOR THE RUN BOI"
        ])

        functions.clear_screen()

        functions.sleeper(
            ["Starting the run"],
            delay=0.5
        )

        going_running(player)

    elif choice_oth == "2":
        going_running(player)

    else:
        print("Choose a valid option dumbfk")


def going_running(player):
    functions.sleeper([
        "Spam ENTER as fast as you can!",
        "GO!"
    ])

    duration = 5
    presses = 0

    start = time.time()

    while time.time() - start < duration:
        input()
        presses += 1

    avg_presses = 6.5 * duration
    fast_threshold = avg_presses * 1.2

    if presses >= fast_threshold:
        functions.sleeper([
            "UGHH YOU RAN TOO FAST MAN"
        ])
        player.change_craving(amount=10)

    elif presses < avg_presses * 0.5:
        functions.sleeper([
            "You barely ran..."
        ])
        player.change_craving(amount=5)

    else:
        functions.sleeper([
            "Nice pace!"
        ])
        player.change_craving(amount=-15)


def craving_lake(player):
    functions.clear_screen()

    functions.sleeper([
        "Hey so welcome to the craving lake",
        "Here you can walk around interact with people and allat",
        "YIPEE finally somewhat of a social life outside ur druggie world"
    ])

    time.sleep(2)

    functions.clear_screen()

    functions.sleeper([
        "Choose your next action:",
        "1. Walk around",
        "2. Thats the only option you got lmao, nvm lets forget about action",
        "Lets js walk twh lwk"
    ])

    functions.clear_screen()

    functions.sleeper([
        "As you were walking you hear a noise from the bush besides you",
        "Choose your next action:",
        "1. Check out what's up",
        "2. Ignore it and walk away from it",
        "3. Throw a rock at it"
    ])

    choice_cl = input("Enter your choice: ")

    if choice_cl == "1":
        functions.sleeper([
            "You take a peek at whats happening",
            "You see bunch of dudes doing drugs"
        ])

        player.change_craving(amount=10)

        functions.sleeper([
            "You continue to walk away"
        ])

    elif choice_cl == "2":
        functions.sleeper([
            "You continue to walk away"
        ])

    elif choice_cl == "3":
        functions.sleeper([
            "Bunch of druggies come rushing at you and beat you up"
        ])

        player.change_health(amount=-30)

        functions.sleeper([
            "You continue to walk away"
        ])

    else:
        print("Choose a valid option dumbfk")

    functions.clear_screen()

    functions.sleeper([
        "As you were walking you see a guy named Scara",
        "He looks hella toxic",
        "What do you want to do?",
        "Choose your next action:",
        "1. Talk to him",
        "2. Walk away"
    ])

    choice_scara = input("Input enter your choice: ")

    if choice_scara == "1":
        functions.sleeper([
            "From craving arises grief; from craving arises fear.",
            "For one who is free from craving, there is no grief—whence fear?",
            "You feel enlightened like shiiiii"
        ])

        player.change_craving(amount=-20)

    elif choice_scara == "2":
        functions.sleeper([
            "You walk away from Scara."
        ])

    else:
        print("Choose a valid option dumbfk")

    functions.clear_screen()

    print("Sorry gangzy but further more its under construction rn")