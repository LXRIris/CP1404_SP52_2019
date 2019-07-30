"""
Replace the contents of this module docstring with your own details
Name: Zwe Nyan Toe
Date started: Does this even really matter
GitHub URL: https://github.com/nelsonnyan2001/SP52_Prog2_Attempt
"""

places_file = open('places.csv', 'r')
places_list_n = places_file.readlines()
places_list = [i.replace("\n", '') for i in places_list_n]


def main():
    print("Travel Tracker 1.0 - by Zwe Nyan Toe")
    menu_choice = main_menu()
    while menu_choice != "q":
        print("yeet")
    exit("User quit program")

def main_menu():
    print("Menu: ")
    print("L - List places")
    print("A - Add places")
    print("M - Mark new place as visited")
    print("Q - Quit")
    menu_choice = input(">>>")
    choices = ["l", "a", "m", "q"]
    menu_choice_l = menu_choice.lower()
    while menu_choice_l not in choices:
        print("Please enter a valid choice.")
        menu_choice = input(">>>")
        menu_choice_l = menu_choice.lower()
    return menu_choice


if __name__ == '__main__':
    main()
