#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: April 5, 2022
# This program asks the user for the length and width
# of shape. then, tell user if the shape is square or
# a rectangle and we do the same thing for triangle as well as
# displaying message for invalid input.


def shape():
    # loop to restart the program
    while True:
        # ask for the length and with of shape as string
        length_string = input("Enter the length of the rectangle ")
        width_string = input("Enter the width of the rectangle ")
        # line space
        print("")
        # convert the input from string to float
        try:
            length_float = float(length_string)
            width_float = float(width_string)
            # check if the shape is square or rectangle
            if length_float == width_float:
                print("Your shape is a square")
                print("")
            else:
                print("Your shape is rectangle")
                print("")
        # display for invalid input
        except Exception:
            print("")
            print("Invalid input. Try Again.")
        # as to restart the program
        restart = input("Restart the program?(y/n or any key to End) ")
        if restart == "y":
            continue
        else:
            break
    print("")
    print("have a good day!")


if __name__ == "__main__":
    shape()
