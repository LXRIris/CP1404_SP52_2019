"""
Replace the contents of this module docstring with your own details
Name: Zwe Nyan Toe
Date started: Does this even really matter
GitHub URL: https://github.com/nelsonnyan2001/SP52_Prog2_Attempt
"""

places_file = open('places.csv', 'r')
places_list_n = places_file.readlines()
places_list = [i.replace("\n", '') for i in places_list_n]
places_file.close()
individual_places_list = []
for i in range(len(places_list)):
    individual_places_list.append(places_list[i].split(','))



def main():
    print("Travel Tracker 1.0 - by Zwe Nyan Toe")
    menu_choice = main_menu()
    while menu_choice != "q":
        if menu_choice == "l":
            print_places()
            menuchoice = main_menu()
        if menu_choice == "a":
            add_menu()

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
        print("Invalid menu choice.")
        menu_choice = input(">>>")
        menu_choice_l = menu_choice.lower()
    return menu_choice


def print_places():
    print("")
    for i in range(len(places_list)):
        print("{:<8} in {:<11} priority {}".format(individual_places_list[i][0], individual_places_list[i][1],
                                                   individual_places_list[i][2]))
    print("")


def add_menu():
    new_name = input("Name: ")
    while new_name == "":
        print("Input cannot be blank.")
        new_name = input("Name: ")
    new_country = input("Country: ")
    while new_country == "":
        print("Input cannot be blank.")
        new_country = input("Country: ")



if __name__ == '__main__':
    main()
