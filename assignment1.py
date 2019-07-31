"""
Replace the contents of this module docstring with your own details
Name: Zwe Nyan Toe
Date started: Does this even really matter
GitHub URL: https://github.com/nelsonnyan2001/SP52_Prog2_Attempt
"""

csv_file = 'places.csv'
places_file = open(csv_file, 'r')
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
    menu_choice_l = input(">>>")
    print("")
    choices = ["l", "a", "m", "q"]
    menu_choice = menu_choice_l.lower()
    while menu_choice not in choices:
        print("Invalid menu choice.")
        print("")
        menu_choice_l = input(">>>")
        print("")
        menu_choice = menu_choice_l.lower()
    while menu_choice != "q":
        if menu_choice == "l":
            print_places()
            main_menu()
        if menu_choice == "a":
            add_menu()
            main_menu()
        if menu_choice == "m":
            mark_menu()
            main_menu()

    write_file = open(csv_file, 'w')
    for place in individual_places_list:
        for item in place:
            write_file.write(item + ",")

        write_file.write("\n")
    write_file.close()
    print("{} places saved to {}".format(len(individual_places_list), csv_file))
    exit("")


def print_places():
    to_visit_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            to_visit_count += 1
            print("*{}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0],
                                                             individual_places_list[i][1],
                                                             individual_places_list[i][2]))
        else:
            print(" {}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0],
                                                             individual_places_list[i][1],
                                                             individual_places_list[i][2]))
    print("")
    if to_visit_count > 0:
        print(" {} places. You still want to visit {} places.".format(len(individual_places_list), to_visit_count))
    else:
        print(" {} places. No places left to visit. Why not add some more?".format(len(individual_places_list)))
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
    print("")
    new_place = [new_name, new_country, new_priority, "n"]
    individual_places_list.append(new_place)


def ask_for_number(message):
    number = 0
    try:
        number = int(input(message))
        while number <= 0:
            print("Number must be more than 0.")
            number = int(input(message))
    except ValueError:
        print("Invalid input, please enter a valid number.")
        ask_for_number(message)
    return number


def mark_menu():
    print_places()
    print("Enter the number of the place to mark as visited.")
    ask_number = ask_for_number(">>>")
    mark_number = ask_number - 1
    non_visited_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            non_visited_count += 1
    if non_visited_count == 0:
        print("No unvisited places.")

    while mark_number > len(individual_places_list):
        print("There aren't that many places.")
        print("Enter the number of the place to mark as visited.")
        ask_number = ask_for_number(">>>")
        mark_number = ask_number - 1
    while individual_places_list[mark_number][3] == "v":
        print("You have already visited that place.")
        print("Enter the number of the place to mark as visited.")
        ask_number = ask_for_number(">>>")
        mark_number = ask_number - 1
    else:
        individual_places_list[mark_number][3] = "v"
        print(
            "{} in {} visited.".format(individual_places_list[mark_number][0], individual_places_list[mark_number][1]))
        print("")


if __name__ == '__main__':
    main()
