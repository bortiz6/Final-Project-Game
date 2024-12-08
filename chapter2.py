import chapter1

def chapter_2():
    print("\n--- CHAPTER 2: THE DUNGEON ---")
    print("You leave your house and enter the dungeon by yourself ignoring people warnings")
    print("A cyclops emerges, blocking your path!")
    chapter_2_scene()

# Scene setup
def chapter_2_scene():
    while True:
        print("\nWhat do you want to do?")
        print("1. Fight the cyclops")
        print("2. Run to the north side")
        print("3. Run to the south side")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            fight_cyclops()
            break
        elif choice == "2":
            print("\nYou decide to run north, escaping the cyclops.")
            print("--- End of Chapter 2 ---")
            chapter_3()  # Move to Chapter 3
            break
        elif choice == "3":
            print("\nYou run south, retreating to where you started.")
            print("You find yourself back in your house.")
            chapter_1()  # Loop back to Chapter 1
            break
        else:
            print("Invalid choice. Try again.")

# Fight the cyclops
import random

def fight_cyclops():
    print("\nYou choose to fight the cyclops")
    print("The cyclops roars and charges at you get ready")
    
    # Simulate fight outcome (50/50 chance)
    outcome = random.choice(["win", "lose"])
    
    if outcome == "win":
        print("\nYou manage to defeat the cyclops after a fierce battle")
        print("As the cyclops dissapears, it drops a golden chest.")
        inventory.append("Golden Chest")
        print("You pick up the golden chest and you move forward.")
        chapter_3()  # Move to Chapter 3
    else:
        print("\nThe cyclops overpowers you in battle.")
        print("It celebrates your defeat with a victorious roar and dances.")
        print("You have died. Game over.")
        print("Would you like to restart the game?")
        restart = input("Enter 'yes' to restart or anything else to quit: ").strip().lower()
        if restart == "yes":
            chapter_1()  # Restart the game
        else:
            print("\nThank you for playing!")
            exit()

# Placeholder for Chapter 3
def chapter_3():
    print("\n--- You sre ready for chapter 3---")

# Inventory management
inventory = []

# Chapter 1 included for context
def chapter_1():
 print("It was a Sunny Morning which was surprising, it was not to be it was supposed to be cloudy with light rain")
 print("You wake up and get ready for an adventure")


# Start the game
chapter_2()