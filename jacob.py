import time
import random

# Constants
MINOR_DAMAGE = 2
MAJOR_DAMAGE = 7
DELAY = random.uniform(1, 5)

# Global Variables
health = 10

def intro():
    print("This is a game where you will make choices.")
    time.sleep(DELAY)
    print("These choices may negatively or positively affect your health. You can die at any point.")
    time.sleep(DELAY)

def first_choice():
    global health
    ans1 = input("Do you approach or run? (approach/run) ").lower()
    if ans1 == "approach":
        print("You approach the thing in the bushes. It is Shia LaBeouf! He bites you and runs away.")
        health -= random.randint(1, MINOR_DAMAGE)
        time.sleep(DELAY)
        print(f"Your health is now: {health}")
        return "follow_shia"
    elif ans1 == "run":
        print("You run and spot a cabin in the distance. However, you trip as you come up to the front door. Ouch")
        health -= random.randint(1, MINOR_DAMAGE)
        time.sleep(DELAY)
        print(f"Your health is now: {health}")
        return "cabin_door"
    else:
        print("Invalid choice. Please try again.")
        return "start"

def follow_shia():
    ans1_2 = input("Do you follow or leave? (follow/leave) ").lower()
    if ans1_2 == "follow":
        time.sleep(DELAY)
        print("You begin to follow him but lose his trail. Instead, you come across a cabin and approach the front door.")
        return "cabin_door"
    elif ans1_2 == "leave":
        print("You lose for being a scaredy cat, smh.")
        return "game_over"
    else:
        print("Invalid choice. Please try again.")
        return "follow_shia"

def cabin_door():
    ans2 = input("Do you open the door? (Y/N) ").upper()
    if ans2 == "Y":
        print("The door swings open. Shia LaBeouf is sat inside watching the TV. You spot an axe.")
        return "axe_decision"
    elif ans2 == "N":
        return "shia_attack"
    else:
        print("Invalid choice. Please try again.")
        return "cabin_door"

def shia_attack():
    global health
    print("It's too late to escape! As you turn, you alert Shia LaBeouf.")
    time.sleep(DELAY)
    print("Shia LaBeouf runs out with a shotgun, aims, and fires.")
    health -= random.randint(MINOR_DAMAGE, MAJOR_DAMAGE)
    time.sleep(DELAY)
    print(f"Your health is {health}")
    if health <= 0:
        print("You have lost. Sorry lad...")
        return "game_over"
    else:
        print("By some miracle you have survived the shot.")
        time.sleep(DELAY)
        print("However, you beg Shia to end your suffering and lose anyway.")
        return "game_over"

def axe_decision():
    ans3 = input("Do you acquire the axe? (Y/N) ").upper()
    if ans3 == "Y":
        print("You grab the axe and hold it over your head as you walk inside.")
        time.sleep(DELAY)
        print("You see your opportunity and swing for Shia LaBeouf.")
        time.sleep(DELAY)
        print("You have succeeded. You win. Shia is dead.")
        print("Well done.")
        return "game_won"
    elif ans3 == "N":
        return shia_attack()
    else:
        print("Invalid choice. Please try again.")
        return "axe_decision"

def main():
    intro()
    name = input("What is your name, adventurer? ")
    print(f"{name}, you are walking through the woods.")
    time.sleep(DELAY)

    next_step = "start"
    while next_step != "game_over" and next_step != "game_won":
        if next_step == "start":
            next_step = first_choice()
        elif next_step == "follow_shia":
            next_step = follow_shia()
        elif next_step == "cabin_door":
            next_step = cabin_door()
        elif next_step == "axe_decision":
            next_step = axe_decision()

    print("Game Over. Thank you for playing!")

if __name__ == "__main__":
    main()
