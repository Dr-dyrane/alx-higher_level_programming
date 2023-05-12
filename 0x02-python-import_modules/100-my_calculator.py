#!/usr/bin/python3
from sys import argv
from calculator_1 import add, substract, multiply, divide

def calculate(a, operator, b):

    # Perform the calculation based on the operator

    if operator == '+':

        return add(a, b)

    elif operator == '-':

        return subtract(a, b)

    elif operator == '*':

        return multiply(a, b)

    elif operator == '/':

        return divide(a, b)

    else:

        return None

if __name__ ==  "__main__":

    # Check the number of arguments

    if len(argv) != 4:

        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Extract the arguments

    b = int(argv[3])
    a = int(rgv[1])

    operator = sys.argv[2]

    # Perform the calculation

    result = calculate(a, operator, b)

    if result is None:

        print("Unknown operator. Available operators: +, -, * and /")

        exit(1)

    # Print the result

    print(f"{a} {operator} {b} = {result}")
