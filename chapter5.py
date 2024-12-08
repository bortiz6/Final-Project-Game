# Chapter 5 Setup



def chapter_5():
    print("\n--- CHAPTER 5: THE FESTIVAL IS IN THE TOWN ---")
    print("You go down a slide and you are back in ground, and you hear voices, so you investigate")
    chapter_5_scene()

# Scene setup
def chapter_5_scene():
    has_interacted = False
    has_taken_tasks = False
    has_rest = False

    while True:
        print("\nWhat do you want to do?")
        print("1. Interact with locals to learn about the festival")
        print("2. Take on tasks to earn money or supplies")
        print("3. Stay at the inn to rest")
        print("4. Move forward to the next chapter")

        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            if not has_interacted:
                interact_with_locals()
                has_interacted = True
            else:
                print("\nYou’ve already spoken with the locals and learned about the festival.")
        elif choice == "2":
            if not has_taken_tasks:
                take_on_tasks()
                has_taken_tasks = True
            else:
                print("\nYou’ve already completed tasks and earned rewards.")
        elif choice == "3":
            if not has_rest:
                rest_at_inn()
                has_rest = True
            else:
                print("\nYou’ve already rested at the inn and feel refreshed.")
        elif choice == "4":
            print("\nYou decide to leave the town and continue your journey.")
            print("--- End of Chapter 5 ---")
            chapter_6()  # Placeholder for next chapter
            break
        else:
            print("Invalid choice. Try again.")

# Interact with locals
def interact_with_locals():
    print("\nYou talk to the locals and learn about the festival.")
    print("They tell you that it’s a celebration of courage, held in honor of past heroes.")
    print("The townsfolk encourage you to join in and explore the festivities.")

# Take on tasks
def take_on_tasks():
    print("\nYou help the locals with various tasks, such as carrying supplies and setting up decorations.")
    print("In return, they reward you with coins and useful items.")
    inventory.append("Coins")
    inventory.append("Food Supplies")
    print("You earned Coins and Food Supplies!")

# Rest at the inn
def rest_at_inn():
    print("\nYou stay at the inn to rest.")
    print("After a good night’s sleep, you feel refreshed and ready for the next part of your journey.")
    print("The innkeeper also gives you a small token of appreciation: a Luck Charm.")
    inventory.append("Luck Charm")

# Placeholder for Chapter 6
def chapter_6():
    print("\n--- CHAPTER 6: TO BE CONTINUED ---")
    print("This chapter is under construction. Stay tuned for more adventures!")

# Inventory management remains the same
inventory = []

# Include previous chapters for context
def chapter_1():
 print("It was a Sunny Morning which was surprising, it was not to be it was supposed to be cloudy with light rain")
 print("You wake up and get ready for an adventure")

def chapter_4():
    print("\n--- CHAPTER 4: THE FLOATING ISLAND ---")
    print('"You climbed up the rope and find yourself on a floating island, surrounded by endless sky."')
    print("Ahead of you is the entrance to the last dungeon. As you step inside, a terrifying hydra appears!")

# Start the game at Chapter 1
chapter_5()
