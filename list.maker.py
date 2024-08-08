import os 
# 2. The Shopping List Maker

# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). Task 2: Include a feature to remove items from the list. Task 3: Add a function that prints out the entire list.


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print('''
___       __    ______                                 _____            ___________            _____________                       _____                    ___________       _____     ______  ___      ______             ______
__ |     / /_______  /__________________ ________      __  /______      __  /___  /______      __  ___/__  /__________________________(_)_____________ _    ___  /___(_)________  /_    ___   |/  /_____ ___  /________________  /
__ | /| / /_  _ \_  /_  ___/  __ \_  __ `__ \  _ \     _  __/  __ \     _  __/_  __ \  _ \     _____ \__  __ \  __ \__  __ \__  __ \_  /__  __ \_  __ `/    __  / __  /__  ___/  __/    __  /|_/ /_  __ `/_  //_/  _ \_  ___/_  / 
__ |/ |/ / /  __/  / / /__ / /_/ /  / / / / /  __/     / /_ / /_/ /     / /_ _  / / /  __/     ____/ /_  / / / /_/ /_  /_/ /_  /_/ /  / _  / / /  /_/ /     _  /___  / _(__  )/ /_      _  /  / / / /_/ /_  ,<  /  __/  /    /_/  
____/|__/  \___//_/  \___/ \____//_/ /_/ /_/\___/      \__/ \____/      \__/ /_/ /_/\___/      /____/ /_/ /_/\____/_  .___/_  .___//_/  /_/ /_/_\__, /      /_____/_/  /____/ \__/      /_/  /_/  \__,_/ /_/|_| \___//_/    (_)   
                                                                                                                   /_/     /_/                 /____/ 
''')

def add_item(shop_list):
    item = input("Enter the item to add: ")
    shop_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item(shop_list):
    item = input("Enter the item to remove: ")
    if item in shop_list:
        shop_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' is not in the list.")

def display_list(shop_list):
    print("Your shopping list:")
    for item in shop_list:
        print(f"- {item}")

def exit():
    print('''
              ____________________                          ______                       _____                    __________       ___________   ________             ______   
______ ____  ____(_)_  /__  /___(_)_____________ _   __________  /__________________________(_)_____________ _    ___  /__(_)________  /___  /   ___  __ )____  _________  /   
_  __ `/  / / /_  /_  __/  __/_  /__  __ \_  __ `/   __  ___/_  __ \  __ \__  __ \__  __ \_  /__  __ \_  __ `/    __  /__  /__  ___/  __/_  /    __  __  |_  / / /  _ \_  /    
/ /_/ // /_/ /_  / / /_ / /_ _  / _  / / /  /_/ /    _(__  )_  / / / /_/ /_  /_/ /_  /_/ /  / _  / / /  /_/ /     _  / _  / _(__  )/ /_  /_/     _  /_/ /_  /_/ //  __//_/     
\__, / \__,_/ /_/  \__/ \__/ /_/  /_/ /_/_\__, /     /____/ /_/ /_/\____/_  .___/_  .___//_/  /_/ /_/_\__, /      /_/  /_/  /____/ \__/ (_)      /_____/ _\__, / \___/(_)      
  /_/                                    /____/                          /_/     /_/                 /____/                                              /____/                
''')

def main():
    welcome()
    shop_list = []
    while True:
        print('''
    Choose an option:

1 - Add item to shopping list
2 - Remove item from shopping list
3 - Display shopping list
4 - Exit the program '''
)
        choice = input("Enter your choice:\n")
        if choice == '1':
            add_item(shop_list)
        elif choice == '2':
            remove_item(shop_list)
        elif choice == '3':
            display_list(shop_list)
        elif choice == '4':
            exit()
            break
        else:
            print("Invalid choice. Please try again.")

main()

