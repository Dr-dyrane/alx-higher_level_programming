# JavaScript - Objects, Scopes, and Closures


## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Rectangle #0](#0-rectangle-0)
  - [1. Rectangle #1](#1-rectangle-1)
  - [2. Rectangle #2](#2-rectangle-2)
  - [3. Rectangle #3](#3-rectangle-3)
  - [4. Rectangle #4](#4-rectangle-4)
  - [5. Square #0](#5-square-0)
  - [6. Square #1](#6-square-1)
  - [7. Occurrences](#7-occurrences)
  - [8. Esrever](#8-esrever)
  - [9. Log me](#9-log-me)
  - [10. Number conversion](#10-number-conversion)
  - [11. Factor index](#11-factor-index)
  - [12. Sorted occurrences](#12-sorted-occurrences)
  - [13. Concat files](#13-concat-files)
- [Getting Started](#getting-started)
- [Author](#author)

## Introduction

This project explores fundamental concepts in JavaScript, including object-oriented programming, scope, and closures. It consists of several tasks that aim to reinforce your understanding of these concepts. In this project, you will work on creating classes, handling inheritance, using prototypes, and more.

## Learning Objectives

By completing this project, you will gain a deeper understanding of the following concepts:

- Creating and using objects in JavaScript.
- Exploring the concept of scope and how it affects variables.
- Understanding closures and their applications.
- Working with inheritance and classes in JavaScript.

## Requirements

- Allowed editors: vi, vim, emacs
- All files must be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file is required at the root of the project directory.
- Your code should follow the semistandard style guide (Rules of Standard + semicolons on top) with the AirBnB style as reference.
- All files must be executable.
- You are not allowed to use the `var` keyword.

## Tasks

### 0. Rectangle #0

Write an empty class `Rectangle` that defines a rectangle.

**Example:**
```javascript
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
```

**Expected Output:**
```
Rectangle {}
[Class: Rectangle]
```

### 1. Rectangle #1

Write a class `Rectangle` that defines a rectangle and initializes it with width and height.

**Example:**
```javascript
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);
```

**Expected Output:**
```
Rectangle { width: 2, height: 3 }
2
3
```

### 2. Rectangle #2

Update the `Rectangle` class to handle invalid inputs for width and height.

### 3. Rectangle #3

Add a `print()` instance method to the `Rectangle` class that prints the rectangle using the character 'X'.

### 4. Rectangle #4

Enhance the `Rectangle` class with methods `rotate()` and `double()`.

### 5. Square #0

Create a class `Square` that inherits from the `Rectangle` class.

### 6. Square #1

Add an instance method `charPrint(c)` to the `Square` class that prints the square using the character `c`.

### 7. Occurrences

Write a function that returns the number of occurrences of an element in a list.

**Example:**
```javascript
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
```

**Expected Output:**
```
1
4
```

### 8. Esrever

Write a function that reverses an array without using the built-in `reverse` method.

**Example:**
```javascript
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
```

**Expected Output:**
```
[5, 4, 3, 2, 1]
```

### 9. Log me

Write a function that prints the number of arguments already printed and the new argument value.

**Example:**
```javascript
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
```

**Expected Output:**
```
0: Hello
1: Best
```

### 10. Number conversion

Write a function that converts a number from base 10 to another base passed as an argument.

**Example:**
```javascript
const converter = require('./10-converter').converter;

const myConverter = converter(16);

console.log(myConverter(12));
console.log(myConverter(89));
```

**Expected Output:**
```
c
59
```

### 11. Factor index

Write a script that computes a new array where each value is the value of the initial list multiplied by its index.

**Example:**
```javascript
const list = require('./100-data').list;
const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
```

### 12. Sorted occurrences

Write a script that computes a dictionary of user IDs by the number of occurrences in a provided dictionary.

**Example:**
```javascript
const dict = require('./101-data').dict;
const sortedDict = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId);
}
console.log(sortedDict);
```

### 13. Concat files

Write a script that concatenates two files and saves the result to a third file.

**Example:**
```bash
$ ./102-concat.js fileA fileB fileC
$ cat fileC
C is fun!
Python is Cool!!!
```

## Getting Started

To get started with this project, follow these steps:

1. Clone the GitHub repository for this project:
   ```
   git clone https://github.com/Dr-dyrane/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```
   cd alx-higher_level_programming/0x13-javascript_objects_scopes_closures
   ```

3. Inside this directory, you will find subdirectories named after the task numbers. Each subdirectory contains the task files, such as `0-rectangle.js`, `1-rectangle.js`, and so on. You will also find example usage files such as `0-main.js`, `1-main.js`, and others.

4. To test a specific task, run the example usage file using Node.js:
   ```
   node 0-main.js
   ```

   Replace `0-main.js` with the appropriate example usage file for the task you want to test.

5. Review the output to see if your code is working as expected. Make any necessary adjustments to your code to ensure it meets the requirements.

## Author

This project is authored by [Alexander Udeogaranya](https://github.com/Dr-dyrane). If you have any questions or need assistance, feel free to contact me through GitHub.