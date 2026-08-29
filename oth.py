import functions
import time
def going_out(player):   
    functions.sleeper([
        "You go outside banging the door loud asl",
        "Your mom screams at you as usual",
        "Hey welcome to the outside world",
        "As for now we are only physically able to go to few places, fuckass addict",
        "so fucking weak"])
    functions.clear_screen()
    functions.sleeper(["Where do u wanna go cutie:",
                        "1. Craving lake",
                        "2. Go running"])
    choice_oth = input ("Enter your choice: ")
    if choice_oth == "1":
        functions.sleeper (["ITS PRETTY FAR VRO YOU HAVE YOU RUN EITHER WAYS",
                           "ABHABAHBAHBAHBA",
                           "ANYWAY GET READY FOR THE RUN BOI"])
    functions.clear_screen()
    functions.sleeper (["Starting the run"], delay=0.5 )

def going_running(player):
    functions.sleeper(["Spam ENTER as fast as you can!", "GO!"])
    
    duration = 5  
    presses = 0
    start = time.time()
    
    while time.time() - start < duration:
        input()
        presses += 1
    
    avg_presses = 6.5 * duration     
    fast_threshold = avg_presses * 1.2  
    
    if presses >= fast_threshold:
        functions.sleeper(["UGHH YOU RAN TOO FAST MAN"])
        player.change_craving(amount=10)
    elif presses < avg_presses * 0.5:  
        functions.sleeper(["You barely ran..."])
        player.change_craving(amount=5)
    else:
        functions.sleeper(["Nice pace!"])
        player.change_craving(amount=-15)

def craving_lake(player):
    functions.sleeper (["sadly its under construction rn hehe"])
    
    

