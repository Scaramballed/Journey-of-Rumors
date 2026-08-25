import functions
import random
import time
import oth

def session(player):
    functions.clear_screen()
    
    if player.study_count >= 3:
        functions.sleeper([
            "You sit down to study...",
            "Your brain is completely fried.",
            "You've been studying too much lately.",
            "You can't focus on anything.",
            "This was a complete waste of time."
        ])
        player.change_craving(amount=30)
        player.study_count += 1
        return after_study_choice(player)
    
    snippets = [
        "print('Hello, world!')",
        "for i in range(10):",
        "if x > 0: print('Positive')",
        "while True: break",
        "def add(a, b): return a + b",
        "class Player: pass",
        "my_list = [1, 2, 3]",
        "for key, value in dict.items():",
        "try: except: pass",
        "return True if x else False"
    ]
    
    target = random.choice(snippets)
    time_limit = 8
    
    functions.sleeper([
        "STUDY SESSION",
        f"You have {time_limit} seconds to type this code:",
        f"\n{target}\n"
    ])
    
    start = time.time()
    answer = input("Type it here: ")
    elapsed = time.time() - start
    
    if elapsed > time_limit:
        functions.sleeper([
            "TIME'S UP!",
            "You were too slow.",
            "That was stressful."
        ])
        player.change_craving(amount=10)
        
    elif answer == target:
        functions.sleeper([
            "PERFECT!",
            "You typed it exactly right.",
            "You feel productive and focused."
        ])
        player.change_craving(amount=-10)
        
    else:
        functions.sleeper([
            "CLOSE, BUT NOT QUITE.",
            f"Expected: {target}",
            f"You typed: {answer}",
            "You're frustrated."
        ])
        player.change_craving(amount=10)
    
    player.study_count += 1
    return after_study_choice(player)


def after_study_choice(player):
    functions.sleeper([
        "Study session complete.",
        "What do you want to do now?"
    ])
    
    while True:
        functions.sleeper([
            "1. Return to your room (pop one)",
            "2. Go outside"
        ])
        choice = input("Enter your choice: ")
        
        if choice == "1":
            functions.sleeper(["You head back to your room."])
            result = functions.pop_one(player)
            return result
            
        elif choice == "2":
            oth.going_out(player)
            return "outside"
            
        else:
            print("Choose a valid option")