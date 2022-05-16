from pickle import TRUE


def user_choice():
    choice = 'wrong'
    within_range = False
    acceptable_range = range(0, 10)

    while choice.isdigit() == False or within_range == False:
        choice = input("please enter a no (0-10): ")
        if choice.isdigit() == False:
            print("sorry that is not a number")
        if choice.isdigit() == TRUE:
            if int(choice) in acceptable_range:
                print("You are in range")
                within_range == TRUE
            else:
                print("sorry you are out of range")
                within_range == False

    return int(choice)


user_choice()
