# Python - Test-driven development

This repository contains solutions to programming exercises in higher-level languages for python test driven development. Python test development involves writing test cases and test suites to verify the functionality and correctness of your code. It helps ensure that your code behaves as expected, handles different scenarios, and maintains reliability. By following best practices and covering edge cases, tests provide confidence in the quality of your code and help detect regressions when making changes or adding new features.

## Table of Contents

1. [Description](#description)
2. [Tasks](#tasks)
3. [Author](#author)

## Description

This repository contains Python programs that solve various programming challenges. Each task is implemented as a separate Python file with corresponding test cases.

## Tasks

### 0. Integers addition

Write a function that adds 2 integers.

Prototype: `def add_integer(a, b=98):`

- `a` and `b` must be integers or floats, otherwise raise a TypeError exception with the message "a must be an integer" or "b must be an integer"
- `a` and `b` must be first casted to integers if they are floats
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### 1. Divide a matrix

Write a function that divides all elements of a matrix.

Prototype: `def matrix_divided(matrix, div):`

- `matrix` must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message "matrix must be a matrix (list of lists) of integers/floats"
- Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message "Each row of the matrix must have the same size"
- `div` must be a number (integer or float), otherwise raise a TypeError exception with the message "div must be a number"
- `div` can't be equal to 0, otherwise raise a ZeroDivisionError exception with the message "division by zero"
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

### 2. Say my name

Write a function that prints "My name is \<first name> \<last name>".

Prototype: `def say_my_name(first_name, last_name=""):`

- `first_name` and `last_name` must be strings, otherwise raise a TypeError exception with the message "first_name must be a string" or "last_name must be a string"
- You are not allowed to import any module

### 3. Print square

Write a function that prints a square with the character #.

Prototype: `def print_square(size):`

- `size` is the size length of the square
- `size` must be an integer, otherwise raise a TypeError exception with the message "size must be an integer"
- If `size` is less than 0, raise a ValueError exception with the message "size must be >= 0"
- If `size` is a float and is less than 0, raise a TypeError exception with the message "size must be an integer"
- You are not allowed to import any module

### 4. Text indentation

Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: `def text_indentation(text):`

- `text` must be a string, otherwise raise a TypeError exception with the message "text must be a string"
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module

### 5. Max integer - Unittest

Write unittests for the function `def max_integer(list=[]):`.

- Your test file should be inside a folder `tests`
- You have to use the `unittest` module

- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.5-max_integer_test`

### 6. Matrix multiplication

Write a function that multiplies 2 matrices.

Prototype: `def matrix_mul(m_a, m_b):`

- `m_a` and `m_b` must be lists of lists of integers or floats, otherwise raise a TypeError exception with the message "m_a must be a list" or "m_b must be a list"
- `m_a` and `m_b` must be matrices with dimensions > 0, otherwise raise a TypeError exception with the message "m_a can't be empty" or "m_b can't be empty"
- `m_a` and `m_b` must be matrices of the same size, otherwise raise a ValueError exception with the message "m_a and m_b can't be multiplied"
- Returns a new matrix
- You are not allowed to import any module

## Author

Alexander Udeogaranya
GitHub: [Dr-dyrane](https://github.com/Dr-dyrane)
