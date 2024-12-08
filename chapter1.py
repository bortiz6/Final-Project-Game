# This will go over Chapter One

def greetings():
 user_name = input("What's your name?")
 print(f"Hello, {user_name}! Welcome to the game")


def chapter_1():
 print("It was a Sunny Morning which was surprising, it was not to be it was supposed to be cloudy with light rain")
 print("You wake up and get ready for an adventure")
 chapter_1_scene()

# Scene setup
def chapter_1_scene():
    has_talked_to_parents = False
    has_gathered_supplies = False

    while True:
        print("\nWhat do you want t0 do?")
        print("1. Talk to your parents")
        print("2. Interact with items to gather supplies")
        print("3. Leave your house")
        print("4. Check your inventory")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            has_talked_to_parents = talk_to_parents()
        elif choice == "2":
            has_gathered_supplies = gather_supplies()
        elif choice == "3":
            if not has_talked_to_parents:
                print("\nYou can't leave yet, Your parents have something important to tell you.")
            elif not has_gathered_supplies:
                print("\nYou can't leave yet, You need supplies for your journey.")
            else:
                print("\nYou left the house, ready for your adventure.")
                print("--- End of Chapter 1 ---")
                chapter_2()  # Move to Chapter 2
                break
        elif choice == "4":
            check_inventory()
        else:
            print("Invalid choice. Try again.")

# Game functions
inventory = []

def talk_to_parents():
    print("\nYour parents look at you thinking how much you grown.")
    print('"Goodmorning," they say, "the journey ahead will be challenging. Goodluck and enjoy your adventure."')
    print("They give you a map to guide you.")
    if "Map" not in inventory:
        inventory.append("Map")
    return True

def gather_supplies():
    supplies = ["Lantern", "Sword", "Snack"]
    for supply in supplies:
        if supply not in inventory:
            print(f"\nYou find and it is a {supply}.")
            inventory.append(supply)
            return True
    print("\nYou've already gathered all the necessary supplies.")
    return True

def check_inventory():
    if inventory:
        print("\nYour inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("\nYour inventory is empty.")

# Placeholder for Chapter 2
def chapter_2():
    print("\n--- You are ready for Chapter 2 ---")

# Start Chapter 1
chapter_1()
