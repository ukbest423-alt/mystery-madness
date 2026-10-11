import random
print("╔══════════════════════════════════╗")
print("║                                  ║")
print("║         MYSTERY MADNESS          ║")
print("║      A Mysterious Adventure      ║")
print("║                                  ║")
print("╚══════════════════════════════════╝")
print()
secret_number = random.randint(1,10)


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

while True:
    try:
        guess = int(input("Guess my secret number between 1 and 10: "))
        break
    except ValueError:
        print("please enter a valid number from 1 to 10! ")
print("you guessed:", guess)

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("too high Try a lower number.")

    while True:
        try:
            guess = int(input("Guess my secret number between 1 and 10: ")) 

            if 1 <= guess <=10:
                break
            else:
                print("Please choose a number from 1 to 10")

        except ValueError:
            print("please enter a valid number!")

print("you have solved my mystery!")

print()
print("============================")
print("         LEVEL 2")
print("      THE SECRET DOOR")
print("============================")
print()
print("you thought you had escaped...")
print("You enter a mysterious room.")
print("two buttons stand before you: RED and BLUE")
print()


has_key = False
door_choice = input("Which button do you press? ").lower()

while door_choice not in ["red", "blue"]:
    print("That isn't one of the buttons! Try again.")
    door_choice = input("choose red or blue: ").lower()

if door_choice == "red":
    print("The room fills with red light!")
    input("press enter to continue...")
    print("A secret key appears on the table.")
    has_key = True

elif door_choice == "blue":
    entrance = "secret passage"
    print("The door unlocks with a loud click...")
    input("press enter to continue...")
    print("you have discovered a secret passage!")

print("You have discovered a treasure chest!")

if has_key == True:
    print("You use the key to open the chest!")
    print("Inside the chest you find some clues!")
    
    clues = [
        " 1. The exit is hidden behind the final maze.",
        " 2. The maze has 3 levels left.",
        " 3. Look for puzzles on the walls"
    ]

    for clue in clues:
        input("press enter to reveal the next clue...")
        print(clue)

else:
    print("The chest is locked! You need a key!")

def enter_level(level, entrance):
    print("===LEVEL", level, "===")
    print("You have entered level", level, "of the maze.")
    print("you have escaped from the", entrance)

def level_4(entrance):
    print()
    print("=======================")
    print("       LEVEL 4")
    print("=======================")
    print()
    print("you have arrived from the ", entrance)
    print("you enter a strange chamber")
    input("Press enter to continue...")
    print("There is a locked exit door at the other end")
    print("You notice several objects scattered around the room")
    inventory = {
        "key": False,
        "torch": False,
        "map": False
    }
    objects = {
        "key": "A rusty key the might unlock the exit.",
        "torch": "An old torch that could light up dark areas",
        "map": "A map showing a hidden passage"
    }
    print("You can see a key, a torch and a map")

    choice = input("which object would you like to inspect? ").lower()

    while choice not in objects:
        print("That object is not in the room. Try again!")
        choice = input("Choose key, torch or map: ").lower()

    print(objects[choice])

    inventory[choice] = True
    print("You collect the", choice + "!")
    print("your inventory:")
    for item, collected in inventory.items():
        if collected:
            print("-", item)


    if choice == "key":
        print("You walk towards the locked exit door.")
        print("You use the key to unlock it!")
        input("Press enter to continue...")
        print("You escape through the main exit and reach Level 5")
        level_5("main exit")


    elif choice == "torch":
        print("You notice a dark passage behind a wall.")
        print("You use the torch to explore the passage.")
        input("Press enter to continue")
        level_5("dark tunnel")

    elif choice == "map":
        print("You study the map and discover a secret route")
        input("Press Enter to continue...")
        print("You follow the map and find a route to Level 5!")
        level_5("secret tunnel")


def level_5(entrance):
    print()
    print("=====================")
    print("      LEVEL 5")
    print("=====================")
    print()
    print("you have arrived from the", entrance)
    print("you enter a new part of the maze.")
    print("you must answer the following riddle to escape once and for all!")
    riddles = [
        ("What has keys but cannot open locks?", "piano"),
        ("What has a face and two hands, but no arms or legs?", "clock"),
        ("What gets wetter as it dries?", "towel")
    ]
    my_riddle, answer = random.choice(riddles)
    print(my_riddle)

    guess = ""

    while guess != answer:
        guess = input("What is your answer? ").lower().strip()

        if guess != answer:
            print("Incorrect! Try again.")

    print()
    print("========================")
    print("     YOU ESCAPED")
    print("========================")
    print()
    print("Congratulations! You solved the final puzzle.")
    print("You have escaped the maze!")


    

def level_3():
    print()
    print("====================================")
    print("             LEVEL 3")
    print("         THE THREE DOORS")
    print("====================================")
    print()
    print("you enter a room with three doors.")
    print("One is red, one is blue and one is green.")
    print()
    

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
                print("you unlock the exit and escape to level 4!")
                level_4("treasure room")
            else:
                print("you try to open the chest but it is locked!")

    elif door == "blue":
        print("you discover a dark underground tunnel")
        input("press enter to continue...")
        print("you walk deeper into the tunnel and discover a locked gate")
        input("press enter to inspect the gate...")
        print("there is a small puzzle carved into the wall")
        
        secret_code = 8
        attempts = 5

        print("the gate requires a secret code")
        print("you have 5 attempts to guess the code")

        while True: 
            try:
                guess = int(input("Enter the secret code: "))
                break
            except ValueError:
                print("Please enter a number!")
                


        while guess != secret_code and attempts > 1:
            attempts = attempts - 1

            if guess <secret_code:
                print("too low, try a higher number.")

            elif guess >secret_code:
                print ("too high, try a lower number.")

            print("attempts left:", attempts)
            while True:
                try: 
                    guess = int(input("try again:"))
                    break
                except ValueError:
                    print("please enter a valid number")

        if guess == secret_code:
            print("correct, the gate unlocks!")
            input("press enter to continue...")
            print("you escape the tunnel and reach level 4!")
            level_4("hidden tunnel")

        else:
            print("you have run out of attempts, the gate remains locked.")
            print("===GAME OVER===")
            print("restart the game to try again.")




    elif door == "green":
        print("you find a mysterious garden.")
        input("press enter to continue...")
        print("you see three strange plants growing next to a locked gate.")
        input("Press enter to inspect the plant..")
        print("One of the plants contains a key that can unlock the gate.")

        plants = ["Rose", "Sunflower", "Moonflower"]

        print("The plants you can search are:")
        for plant in plants:
            print(plant)

        plant_choice = input("Which plant do you want to search? ").lower()

        while plant_choice != "rose" and plant_choice != "sunflower" and plant_choice != "moonflower":
            print("That is not an option. Try again!")
            plant_choice = input("Choose rose, sunflower of moonflower: ").lower()

        has_green_key = False

        while has_green_key == False:
            if plant_choice == "moonflower":
                print("you search the moonflower and find a small key!")
                has_green_key = True
            else:
                print("you search the plant but there is no key here.")
                plant_choice = input("try another plant: ").lower()

                while plant_choice != "rose" and plant_choice != "sunflower" and plant_choice != "moonflower":
                    print("That is not one of the plants! Try again!")
                    plant_choice = input("Choose rose,sunflower or moonflower: ").lower()

        if has_green_key == True:
            input("press enter to continue...")
            print("you use the key to unlock the garden gate!")
            input("press enter to continue...")
            print("you escape the garden and reach level 4!")
            level_4("mysterious garden")



level_3()








