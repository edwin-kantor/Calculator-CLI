#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator CLI - Main Program

A simple command-line calculator for basic mathematical operations.
"""

from utils import add, subtract, multiply, divide, get_number_input, get_choice

def display_menu():
    """
    Display the calculator menu
    """
    print("-----Calculator Menu-----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    print("--------------------")


def perform_calculation(choice):
    """
    Perform the selected calculation
    
    Args:
        choice: Menu choice (1-4)
    
    Returns:
        Boolean indicating success
    """
#Here we will ask the user for a number.

    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

#Then we will perform the chosen operation.

    if choice == 1:
     result = add(num1, num2)
     print("The result is: ", result)

    elif choice == 2:
        result = subtract(num1, num2)
        print("The result is: ", result)

    elif choice == 3:
        result = multiply(num1, num2)
        print("The result is: ", result)

    elif choice == 4:
        try:
            result = divide(num1, num2)
            print("Result:", result)
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            return False

    return True

def main():
    """
    Main program loop
    """

    print("Welcome to the Calculator Program!")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 5:
            print("Exiting calculator. Goodbye!")
            break

        # Perform the chosen operation
        perform_calculation(choice)

        # Ask user if they want another calculation
        again = input("Do you want to perform another calculation? (Y/N): ").lower()

        # FIXED: Exit when user types anything except "y"
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()