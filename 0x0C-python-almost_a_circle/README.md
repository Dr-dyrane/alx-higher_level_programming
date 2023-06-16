# Python - Almost a Circle

This project is part of the ALX Higher Level Curriculum and focuses on various aspects of Python programming, including object-oriented programming, unit testing, file handling, and serialization.

## Description

The "Python - Almost a Circle" project is designed to explore and reinforce your knowledge of Python programming concepts. You will implement classes and functionalities related to rectangles and squares, covering topics such as inheritance, class attributes, instance attributes, getter/setter methods, serialization/deserialization, and unit testing.

## Getting Started

To get started with the project, follow these steps:

1. Clone the project repository:

   ```bash
   git clone https://github.com/Dr-dyrane/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-higher_level_programming/0x0C-python-almost_a_circle
   ```

3. Run the unit tests:

   ```bash
   python3 -m unittest discover tests
   ```

## Learning Objectives

By completing this project, you will gain knowledge and understanding of the following topics:

- Unit testing and its implementation in a large project
- Serialization and deserialization of Python objects
- Reading and writing JSON files
- Usage of `*args` and `**kwargs` in function parameters
- Handling named arguments in functions

## File Structure

The project directory is structured as follows:

- `models/`: This directory contains the Python modules implementing the classes.

  - `base.py`: Contains the `Base` class, which serves as the base for other classes.
  - `rectangle.py`: Implements the `Rectangle` class, a subclass of `Base` representing a rectangle.
  - `square.py`: Implements the `Square` class, a subclass of `Rectangle` representing a square.

- `tests/`: This directory contains the unit tests for the project.

  - `test_models/`: This directory contains the test modules for the models.
    - `test_base.py`: Contains unit tests for the `Base` class.
    - `test_rectangle.py`: Contains unit tests for the `Rectangle` class.
    - `test_square.py`: Contains unit tests for the `Square` class.

- `README.md`: This file provides an overview and instructions for the project.

## Requirements

- Python 3.8.5
- pycodestyle 2.8.\*
- Ubuntu 20.04 LTS

## Author

This project is authored by [Alexander Udeogaranya](https://github.com/Dr-dyrane/alx-higher_level_programming.git/tree/master/0x0C-python-almost_a_circle).
