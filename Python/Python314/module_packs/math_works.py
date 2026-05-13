"""
Custom exhaustive module on mathematical concepts
"""

import cmath


def quadratic_equation(a: int, b: int, c: int):
    """
    Solves quadratic equations of ax² + bx + c = 0 format
    """
    try:
        x_1 = 0
        x_2 = 0
        determinant = b**2 - (4 * a * c)
        if determinant >= 0:
            x_1 = (-b + determinant**0.5) / (2 * a)
            x_2 = (-b - determinant**0.5) / (2 * a)
            return f"{x_1} and {x_2}"
        x_1 = (-b + (cmath.sqrt(determinant))) / (2 * a)
        x_2 = (-b - (cmath.sqrt(determinant))) / (2 * a)
        return f"{x_1} and {x_2}"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Input valid values"
    except TypeError:
        return "Input integers or floats"


def square_limit_finder(limit: int, step: int = 1):
    """
    Finds the highest numbers having
    its square between 0 and the limit
    """
    iteration = 0
    try:
        while iteration**2 <= limit:
            iteration += step
        return iteration - 1
    except ValueError:
        return "Re-enter values to be used"
    except TypeError:
        return "Inappropriate value type"


def factorial(number: int):
    """
    Find the factorial of a number
    """
    iteration = 1
    number_factorial = number
    while iteration < number:
        number_factorial *= number - iteration
        iteration += 1
    return number_factorial


def add(number_1, number_2):
    "Basic additive function"
    return number_1 + number_2


def subtract(number_1, number_2):
    "Basic subtractive function"
    return number_1 - number_2


def divide(number_1, number_2):
    "Basic divisive function"
    return number_1 / number_2


def multiply(number_1, number_2):
    "Basic multiplicative function"
    return number_1 * number_2


def calculate():
    """
    Calculator for +, -, *, / operations
    """
    number_1 = float(input("number_1: "))
    while True:
        try:
            operation = input("operation: ")
            if operation == "quit":
                break
            number_2 = float(input("number_2: "))
            if operation == "+":
                number_1 = add(number_1, number_2)
                continue
            if operation == "-":
                number_1 = subtract(number_1, number_2)
                continue
            if operation == "/":
                number_1 = divide(number_1, number_2)
                continue
            if operation == "*":
                number_1 = multiply(number_1, number_2)
                continue
        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError:
            return "Error: Invalid input"
        except TypeError:
            return "Error: Invalid value type"
    return number_1
