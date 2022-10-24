#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 21, 2022
# This program calculates the roots of quadratic equations

from termcolor import colored
import root_calculator

# Defining the color selection function
def color_selection():

    # Displays the colors
    print("COLOR MENU\n=========")
    colors = ["Red", "Blue", "Yellow", "Grey", "Green", "Magenta", "Cyan", "White"]
    num = 0
    for i in colors:
        num += 1
        print(f"{num}. {i}")

    # Get's the user's color choice
    user_color = input("Choose a color from the list : ")

    # Tries casting user_color to an integer
    try:
        user_color = int(user_color)

    # Restarts the function after a key is entered
    except ValueError:
        print("You must enter an integer.")
        return color_selection()

    # Makes color variable available to main function
    global color

    # Match-case structure for color choices
    match user_color:
        case 1:
            color = "red"
        case 2:
            color = "blue"
        case 3:
            color = "yellow"
        case 4:
            color = "grey"
        case 5:
            color = "green"
        case 6:
            color = "magenta"
        case 7:
            color = "cyan"
        case 8:
            color = "white"
        case _:

            # Restarts the function if an invalid input is given
            print("Invalid input, choose a number from the list.")
            input("Enter any key to restart:\n")
            color_selection()


def main():

    # Calls the color function
    color_selection()

    # Getting the 'a' value of the quadratic from the user:
    a = input(colored("Enter the 'a' value of the quadratic: ", color))
    # Loop triggered if the 'a' variable receives a value of "0":
    while a == "0":
        print(colored("'a' cannot be zero.", color))
        a = input(colored("Enter the 'a' value of the quadratic: ", color))

    # Tests if the 'a' value is a number:
    try:
        a = float(a)

    # Exception thrown if 'a' is not a number
    except ValueError:

        # Tells the user to enter a number that is not 0:
        print(colored("Please enter a valid number that is not 0", color))
        while not isinstance(a, float):
            a = input(colored("Enter the 'a' value of the quadratic: ", color))

            # Loop triggered if the user entered a 0:
            while a == "0":
                print(colored("Enter an 'a' value other than 0.", color))
                a = input(colored("Enter the 'a' value of the quadratic: ", color))

            # Tests if the 'a' value is a number:
            try:
                a = float(a)
            except ValueError:
                print(colored("You did not enter a valid number.", color))

    # Getting the 'b' value of the quadratic from the user.
    b = input(colored("Enter the 'b' value of the quadratic: ", color))

    # Tests if the 'b' value is a number:
    try:
        b = float(b)

    # Exception thrown if 'b' is not a number
    except ValueError:
        print(colored("You did not enter a number", color))

        # Loops continues until 'b' is given a numeric value
        while not isinstance(b, float):
            b = input(colored("Enter the 'b' value of the quadratic: ", color))
            try:
                b = float(b)
                break
            except ValueError:
                print(colored("You did not enter a number", color))

    # Getting the 'c' value of the quadratic from the user.

    c = input(colored("Enter the 'c' value of the quadratic: ", color))

    # Tests if the 'c' value is a number:
    try:
        c = float(c)

    # Exception thrown if 'c' is not a number
    except ValueError:
        print(colored("You did not enter a number", color))

        # Continues to ask the user for a valid number until given such.
        while not isinstance(c, float):
            c = input(colored("Enter the 'a' value of the quadratic: ", color))
            try:
                c = float(c)
            except ValueError:
                print(colored("You did not enter a number", color))

    # Calls the root solver function to solve the quadratic
    from root_calculator import root_solver

    root_solver(a, b, c)


if __name__ == "__main__":

    # Runs the main function
    main()

    # Asks the user if they would like to restart
    print(colored("Enter 'y' if you would like to restart", color))
    restart = input(colored("Enter anything else to stop the program: ", color))

    # Repeats the program until a character other than 'y' is entered for the restart
    # variable
    while restart == "y":
        main()
        print(colored("Enter anything else to stop the program: ", color))
        restart = input(colored("Enter 'y' if you would like to restart: ", color))
