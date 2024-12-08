# Chapter 3 Setup

def chapter_3():
    print("\n--- CHAPTER 3: TRAPPED IN THE ABANDONED DUNGEON ---")
    print('"You open the next dungeon and accidently activated a switch trapping you, but you see a huge whole in the ceiling"')
    chapter_3_scene()

# Scene setup
def chapter_3_scene():
    has_key = False
    has_rope = False

    while True:
        print("\nWhat do you want to do?")
        print("1. Walk north to see if the door opens")
        print("2. Walk west to open the door")
        print("3. Walk east to open the door")
        print("4. Interact with the rope")
        print("5. Go up the rope")

        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\nYou walk north to check the door, but it doesn’t open.")
        elif choice == "2":
            print("\nYou walk west and find a door, but there's nothing there.")
        elif choice == "3":
            if not has_key:
                print("\nYou walk east and discover a hidden key.")
                has_key = True
                inventory.append("Key")
            else:
                print("\nYou’ve already picked up the key.")
        elif choice == "4":
            if has_key:
                print("\nYou test the rope, and it seems strong enough to hold your weight.")
                has_rope = True
            else:
                print("\nYou inspect the rope, but it feels unsafe. You can’t use it without the key.")
        elif choice == "5":
            if has_rope:
                print("\nYou climb up the rope and escape through the hole in the ceiling.")
                print("--- End of Chapter 3 ---")
                chapter_4()  # Move to Chapter 4
                break
            else:
                print("\nYou can’t climb the rope yet. Ensure it’s strong enough first!")
        else:
            print("Invalid choice. Try again.")

# Placeholder for Chapter 4
def chapter_4():
    print("\n--- Ready for Chapter 4 ---")

# Inventory management
inventory = []

# Include previous chapters and functions for context
def chapter_1():
 print("It was a Sunny Morning which was surprising, it was not to be it was supposed to be cloudy with light rain")
 print("You wake up and get ready for an adventure")

def chapter_2():
    print("\n--- CHAPTER 2: THE DUNGEON ---")
    print("You leave your house and enter the dungeon by yourself ignoring people warnings")
    print("A cyclops emerges, blocking your path!")

# Inventory management, fight cyclops, gather supplies, etc., remain the same.

# Start Chapter 1
chapter_3()


