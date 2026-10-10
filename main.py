import random
secret_number = random.randint(1,10)

print("=====MYSTERY MADNESS=====")
print("Welcome, you must guess my secret number in order to pass.")
print("Can you solve my mystery?")

name = input("What is your name? ")
print("Welcome to the game, " + name + "!")

colour = input("What is your favourite colour? ").lower()
print("Ah i see, " + colour + " is a great choice!")

if colour == "purple":
    print("purple is the colour of magic!")

elif colour == "blue":
    print("blue is the colour of mystery!")

elif colour == "green":
    print("green is the colour of nature!")

else:
    print("thats an interesting colour!")

guess = int(input("Guess my secret number between 1 and 10: "))
print("you guessed:", guess)

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("too high Try a lower number.")

    guess = int(input("Guess my secret number between 1 and 10: ")) 

print("you have solved my mystery!")

print("you have not escaped yet...")
print("LEVEL 2: The Secret Door")
print("There are two buttons, red and blue, you must choose one, " + name + ".")

has_key = False
door_choice = input("Which button do you press? ").lower()

while door_choice != "red" and door_choice != "blue":
    print("That isn't one of the buttons! Try again.")
    door_choice = input("choose red or blue: ").lower()

if door_choice == "red":
    print("The room fills with red light!")
    input("press enter to continue...")
    print("A secret key appears on the table.")
    has_key = True

elif door_choice == "blue":
    print("The door unlocks with a loud click...")
    input("press enter to continue...")
    print("you have discovered a secret passage!")

print("You have discovered a treasure chest!")

if has_key == True:
    print("You use the key to open the chest!")
    print("Inside the chest you find some clues!")
    
    clues = [
        " 1. The exit is hidden behind the final door.",
        " 2. The maze has 3 levels left.",
        " 3. Look for symbols on the doors"
    ]

    for clue in clues:
        input("press enter to reveal the next clue...")
        print(clue)

else:
    print("The chest is locked! You need a key!")

def level_3():
    print ("===LEVEL 3===: The Three Doors")
    print("You enter a room with three doors.")
    print("One is red, one is blue, and one is green")

    door = input("which door do you choose: red, blue or green? ").lower()

    while door != "red" and door != "blue" and door != "green":
        print("that is not an option. Try again!")
        door = input("Choose red, blue or green: ").lower()

    if door == "red":
        print("you enter a room full of treasure!")
        has_red_key = False
        input("press enter to search the room...")
        print("you find a small key hidden in a pile of gold!")
        has_red_key = True

        input("press enter to continue...")
        print("You spot a locked chest in the corner!")

        chest_choice = input("Do you want to open the chest? yes or no: ").lower()

        while chest_choice != "yes" and chest_choice != "no":
            print("That is not an option. Try again!")
            chest_choice = input("do you want to open the chest? yes or no: ").lower()

        while chest_choice == "no":
            print("Are you sure? There might be something important inside...")
            chest_choice = input("do you want to open the chest? yes or no: ").lower()

            while chest_choice != "yes" and chest_choice != "no":
                print("That is not an option. Try again!")
                chest_choice = input("do you want to open the chest? yes or no: ").lower()

        if chest_choice == "yes":
            if has_red_key == True:
                print("you use the key to unlock the chest!")
                input("press enter to continue...")
                print("inside you find a key to the exit")
                input("press enter to continue...")
                print("you unlock the exite and escape to level 4!")
            else:
                print("you try to open the chest but it is locked!")

    elif door == "blue":
        print("you discover a dark underground tunnel")
        input("press enter to continue...")

    elif door == "green":
        print("you find a mysterious garden.")



level_3() 







