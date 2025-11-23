#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator CLI - Main Program

A simple command-line calculator for basic mathematical operations.
"""

# TODO 🇺🇸: Import utility functions from utils.py
from utils import add, subtract, multiply, divide, get_number_input, get_choice


def display_menu():
    """
    Display the calculator menu
    """
    # TODO 🇺🇸: Print menu with operations and exit option
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
    # TODO 🇺🇸: Get two numbers from user, call appropriate operation function based on choice, and display result or error message

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
    # TODO 🇺🇸: Create infinite loop, display menu and get user choice, handle exit option, and ask if user wants another calculation
    
print("Welcome to the Calculator Program!")

while True:
    display_menu()
    choice = get_choice()

    if choice == 5:
        print("Exciting calculator. Goodbye!")
        break

    #Here we will run the chosen operation
    perform_calculation(choice)

    #Here we will ask the user if he want to calculate again.
    again = input("Do you want to perform another calculation? (Y/N): ").lower()

    if again == "y":
        perform_calculation(choice)
        again = input("Do you want to perform another calculation? (Y/N): ").lower()
        if again == "n":
            break

if __name__ == "__main__":
    main()