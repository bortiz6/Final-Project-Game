

# Chapter 4 Setup
def chapter_4():
    print("\n--- CHAPTER 4: THE FLOATING ISLAND ---")
    print("You climbed up the rope where you enter a floating island and enter the last dungeon")
    chapter_4_scene()

# Scene setup
def chapter_4_scene():
    while True:
        print("\nWhat do you want to do?")
        print("1. Fight the hydra")
        print("2. Run to the north")
        print("3. Run to the south")

        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            fight_hydra()
            break
        elif choice == "2":
            print("\nYou decide to run north, leaving the hydra behind.")
            print("--- End of Chapter 4 ---")
            chapter_5()  # Move to Chapter 5
            break
        elif choice == "3":
            print("\nYou run south, retreating back to the previous dungeon.")
            chapter_3()  # Loop back to Chapter 3
            break
        else:
            print("Invalid choice. Try again.")

# Fight the hydra
def fight_hydra():
    print("\nYou choose to fight the hydra!")
    print("The hydra roars, its many heads snapping at you.")
    
    # Simulate fight outcome (50/50 chance)
    import random
    outcome = random.choice(["win", "lose"])
    
    if outcome == "win":
        print("\nAfter a grueling battle, you manage to defeat the hydra!")
        print("As it collapses, you discover a piece of enchanted armor.")
        inventory.append("Enchanted Armor")
        print("You equip the armor and prepare to continue your journey.")
        chapter_5()  # Move to Chapter 5
    else:
        print("\nThe hydra overwhelms you with its might.")
        print("You fall to its powerful attacks. Game over.")
        print("Would you like to restart the game?")
        restart = input("Enter 'yes' to restart or anything else to quit: ").strip().lower()
        if restart == "yes":
            chapter_1()  # Restart the game
        else:
            print("\nThank you for playing!")
            exit()

# Placeholder for Chapter 5
def chapter_5():
    print("\n--- Ready for Chapter 5 ---")

# Inventory management remains the same
inventory = []

# Include previous chapters and functions for context
def chapter_1():
 print("It was a Sunny Morning which was surprising, it was not to be it was supposed to be cloudy with light rain")
 print("You wake up and get ready for an adventure")

def chapter_3():
 print("\n--- CHAPTER 3: TRAPPED IN THE ABANDONED DUNGEON ---")
 print('"You open the next dungeon and accidently activated a switch trapping you, but you see a huge whole in the ceiling"')
# Start Chapter 1
chapter_4()
