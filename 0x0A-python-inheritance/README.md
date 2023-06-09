# Python Inheritance

This project explores the concept of inheritance in Python and its various aspects. It covers superclass, subclass, method overriding, multiple inheritance, and more. The project aims to enhance your understanding of object-oriented programming (OOP) and the advantages of using inheritance in Python.

## Learning Objectives

Upon completing this project, you should be able to:

- Explain why Python programming is awesome
- Understand superclass, baseclass, or parentclass
- Identify and define subclasses
- List all attributes and methods of a class or instance
- Understand when an instance can have new attributes
- Inherit a class from another class
- Define a class with multiple base classes
- Recognize the default class every class inherits from
- Override a method or attribute inherited from the base class
- Utilize attributes or methods available to subclasses through inheritance
- Understand the purpose and benefits of inheritance
- Use `isinstance`, `issubclass`, `type`, and `super` built-in functions effectively

## Files and Usage

- `0-lookup.py`: Contains a function `def lookup(obj):` that returns a list of available attributes and methods of an object.
- `1-my_list.py`: Implements a class `MyList` that inherits from the `list` class and adds a method `def print_sorted(self):` to print the list in ascending order.
- `2-is_same_class.py`: Defines a function `def is_same_class(obj, a_class):` that checks if an object is an instance of a specified class.
- `3-is_kind_of_class.py`: Defines a function `def is_kind_of_class(obj, a_class):` that checks if an object is an instance of a class or an instance of a class that inherited from the specified class.
- `4-inherits_from.py`: Defines a function `def inherits_from(obj, a_class):` that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
- `5-base_geometry.py`: Contains an empty class `BaseGeometry` as the base class for other classes related to geometry.
- `6-base_geometry.py`: Updates the `BaseGeometry` class with a method `def area(self):` that raises an exception with a message.
- `7-base_geometry.py`: Further updates the `BaseGeometry` class by adding a method `def integer_validator(self, name, value):` that validates the `value` parameter.
- `8-rectangle.py`: Defines a class `Rectangle` that inherits from `BaseGeometry` and adds width and height attributes.
- `9-rectangle.py`: Extends the `Rectangle` class by implementing the `area` method.
- `10-square.py`: Defines a class `Square` that inherits from `Rectangle` and adds a size attribute.
- `100-my_int.py`: Defines a class `MyInt` that inherits from `int` and overrides the `==` and `!=` comparison operators.
- `101-add_attribute.py`: Defines a function `def add_attribute(obj, attribute, value):` that adds a new attribute to an object if possible.

## Testing

Unit tests for the implemented classes and functions can be found in the `tests` directory. To run the tests, execute the following command:
```
python3 -m doctest ./tests/*
```

## Author

This project was created by [Alexander Udeogaranya](https://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@github.com/Dr-dyrane/alx-higher_level_programming/tree/master/0x0A-python-inheritance) for the Python Inheritance module of the ALX Software Engineering program.
