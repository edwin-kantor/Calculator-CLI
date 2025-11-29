#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator CLI - Utility Functions

Helper functions for calculator operations and input validation.
"""


def add(num1, num2):
    """
    Perform addition
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Sum of the two numbers
    """
    # TODO 🇺🇸: Return the sum of num1 and num2
    return num1 + num2

def subtract(num1, num2):
    """
    Perform subtraction
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Difference of the two numbers
    """
    # TODO 🇺🇸: Return the difference of num1 and num2
    return num1 - num2

def multiply(num1, num2):
    """
    Perform multiplication
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Product of the two numbers
    """
    # TODO 🇺🇸: Return the product of num1 and num2
    return num1 * num2

def divide(num1, num2):
    """
    Perform division
    
    Args:
        num1: Dividend
        num2: Divisor
    
    Returns:
        Quotient
    
    Raises:
        ZeroDivisionError: If divisor is zero
    """
    # TODO 🇺🇸: Check if num2 is zero (raise ZeroDivisionError if so), then return the quotient of num1 and num2
    if num2 == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return num1 / num2

def get_number_input(prompt):
    """
    Get and validate numeric input from user
    
    Args:
        prompt: Input prompt message
    
    Returns:
        Valid float number
    """
    # TODO 🇺🇸: Create infinite loop for input validation, use try-except to handle ValueError, return valid float when input is correct, and print error message on invalid input
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_choice():
    """
    Get user's menu choice
    
    Returns:
        Valid choice (1-5)
    """
    # TODO 🇺🇸: Create infinite loop for input validation, get user input and convert to integer, validate that choice is between 1-5, and return valid choice or display menu again on error
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice >= 1 and choice <= 5:
                return choice
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")

