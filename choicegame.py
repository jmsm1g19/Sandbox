#This is a game of choice!
import time
import random
delay = random.random() * 4 + 1
#Setting health at 10 for the beginning of the game.
health = 10
#Introduction to the game
print("This is a game where you will make choices.")
time.sleep(delay)
print("These choices may negatively or positively affect your health. You can die at any point.")
time.sleep(delay)
print("Your health starts at 10.")
time.sleep(delay)
#Game begins
name = input("What is your name, adventurer?")
print(name + ", you are walking through the woods.")
time.sleep(delay)
print("You spot something moving in the bushes.")
time.sleep(delay)
#First choice: to approach or run from bushes
ans1 = input("Do you approach or run? (approach/run)")
if ans1 == "approach":
    print("You approach the thing in the bushes. It is Shia LaBeouf! He bites you and runs away.")
    bite = int(random.random() * 4 + 2)
    health -= bite
    time.sleep(delay)
    print("Your health is now: " + str(health))
    time.sleep(delay)
    #Choose to follow or run after Shia.
    print("You can see the direction in which Shia LaBeouf has run.")
    time.sleep(delay)
    ans1_2 = input("Do you follow or leave? (follow/leave)")
    if ans1_2 == "follow":
        time.sleep(delay)
        #Cabin is introduced. Now progresses to next bit of code.
        print("You begin to follow him but you lose his trail. Instead you come across a cabin and approach the front door.")
    if ans1_2 == "leave":
        #Game is lost is the choice to leave is made.
        time.sleep(delay)
        print("You lose for being a scaredy cat, smh.")
        health = 0
        time.sleep(delay)
        print("You have lost. What a shame lmao. Your health is " + str(health))
        time.sleep(delay)
        exit ()
if ans1 == "run":
    #If player chooses to run, some damage is taken.
    print("You run and spot a cabin in the distance. However, you trip as you come up to the front door. Ouch")
    trip = int(random.random() * 2 + 1)
    health -= trip
    time.sleep(delay)
    print("Your health is now: " + str(health))
#Both answers for the first choice are concluded. Player will either progress onwards or their game has ended already.
print("You walk up to the cabin door.")
time.sleep(delay)
ans2 = input("Do you open the door? (Y/N)")
if ans2 == "Y":
    print("The door swings open. Shia LaBeouf is sat inside watching the TV. You spot an axe.")
if ans2 == "N":
    print("It's too late to escape! As you turn, you alert the resident. ")
    time.sleep(delay)
    print("Shia LaBeouf runs out with a shot gun, aims and fires.")
    gun = int(random.random() * 7 + 3)
    health -= gun
    time.sleep(delay)
    print("Your health is " + str(health))
    time.sleep(delay)
    if health <= 0:
        print("You have lost. Sorry lad...")
    if health > 0:
        print("By some miracle you have survived the shot.")
        time.sleep(delay)
        print("However, you beg Shia to end your suffering and lose anyway.")
    exit()
ans3 = input("Do you aquire the axe? (Y/N)")
if ans3 == "Y":
    print("You grab the axe and hold it over your head as you walk inside.")
    time.sleep(delay)
    print("You see your opportunity and swing for Shia LaBeouf.")
    time.sleep(delay)
    #Potentially introduce a time reaction game here to gamify the ending?
    print("You have succeeded. You win. Shia is dead.")
    time.sleep(delay)
    print("Well done.")
if ans3 == "N":
    print("As you step away from the axe, you make a noise and Shia LaBeouf spots you.")
    time.sleep(delay)
    print("You turn to run but he has grabbed a shotgun, aims it and fires at you.")
    time.sleep(delay)
    #A repeat of earlier code to save time. Could be altered!
    gun = int(random.random() * 7 + 3)
    health -= gun
    print("Your health is " + str(health))
    time.sleep(delay)
    if health <= 0:
        print("You have lost. Sorry lad...")
    if health > 0:
        print("By some miracle you have survived the shot.")
        time.sleep(3)
        print("However, you beg Shia to end your suffering and lose anyway.")
    exit()
