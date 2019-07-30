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
    main_menu()
    exit("User quit program")


def main_menu():
    print("Menu: ")
    print("L - List places")
    print("A - Add places")
    print("M - Mark new place as visited")
    print("Q - Quit")
    print("")
    menu_choice = input(">>>")
    choices = ["l", "a", "m", "q"]
    menu_choice_l = menu_choice.lower()
    while menu_choice_l not in choices:
        print("Invalid menu choice.")
        print("")
        menu_choice = input(">>>")
        menu_choice_l = menu_choice.lower()
    while menu_choice != "q":
        if menu_choice == "l":
            print_places()
            main_menu()
        if menu_choice == "a":
            add_menu()
            main_menu()


def print_places():
    print("")
    to_visit_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            to_visit_count += 1
            print("*{}. {:<8} in {:<11} priority {}.".format(i, individual_places_list[i][0], individual_places_list[i][1],
                                                       individual_places_list[i][2]))
        else:
            print(" {}. {:<8} in {:<11} priority {}.".format(i, individual_places_list[i][0], individual_places_list[i][1],
                                                         individual_places_list[i][2]))
    print("")
    print(" {} places. You still want to visit {} places.".format(len(individual_places_list), to_visit_count))
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
    new_priority = ask_for_number("Please input a priority: ")
    print("{} in {} (priority {}) added to Travel Tracker".format(new_name, new_country, new_priority))
    new_place = []
    new_place.append(new_name)
    new_place.append(new_country)
    new_place.append(new_priority)
    individual_places_list.append(new_place)


def ask_for_number(message):
    number = 0
    try:
        number = int(input(message))
        while number <= 0:
            print("Priority must be more than 0.")
            number = int(input(message))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        ask_for_number(message)
    return number




if __name__ == '__main__':
    main()
