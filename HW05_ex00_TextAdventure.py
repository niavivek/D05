#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import argv
from sys import exit

# Body

# global variable
user_name = ""
def infinite_stairway_room(count=0):
    global user_name
    print("%s walks through the door to see a dimly lit hallway." % user_name)
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('%s take\'s the stairs' % user_name)
        if (count > 0):
            print("but %s is not happy about it" % user_name)
        infinite_stairway_room(count + 1)
    option_2 = "open door"
    if next == option_2:
        gold_room()
    else:
        dead("Dead in a dark room")


def gold_room():
    global user_name
    print("This room is full of gold.  How much do you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("%s, learn to type a number." % user_name)

    if how_much < 50:
        print("Nice, %s is not greedy, %s wins!" % (user_name, user_name))
        exit(0)
    else:
        dead("%s greedy goose!" % user_name)


def bear_room():
    global user_name
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is %s going to move the bear?" % user_name)
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey" or next == "take" or next == "honey":
            dead("The bear looks at %s then slaps your face off." % user_name)
        elif next == "taunt bear" or next == "taunt" and not bear_moved:
            print("The bear has moved from the door. %s can go through it now." % user_name)
            bear_moved = True
        elif next == "taunt bear" or next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off." % user_name)
        elif next == "open door" or next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    global user_name
    print("Here %s sees the great evil Cthulhu." % user_name)
    print("He, it, whatever stares at %s and %s goes insane." % (user_name, user_name))
    print("Does %s flee for %s's life or eat %s's head?" % (user_name, user_name, user_name))

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    global user_name
    script_name, user_name = argv
    print("%s is in a dark room." % user_name)
    print("There is a door to %s's right and left." % user_name)
    print("Which one does %s take?" % user_name)

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("%s stumble's around the room until you starve." % user_name)

if __name__ == '__main__':
    main()
