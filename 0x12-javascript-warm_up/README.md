# JavaScript Warm-Up Project

## Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Getting Started](#getting-started)
- [File Descriptions](#file-descriptions)
- [Author](#author)

## Project Description

This repository contains a series of JavaScript warm-up tasks designed to help you solidify your understanding of fundamental JavaScript concepts. You will be working on various scripting exercises that cover topics such as variables, control flow, functions, objects, and more. The goal of this project is to improve your familiarity with JavaScript as a programming language and prepare you for more advanced projects that involve web front-end development and dynamic scripting.

## Learning Objectives

By completing the tasks in this project, you will achieve the following learning objectives:

- Gain a deeper understanding of JavaScript programming.
- Learn how to create and use variables and constants.
- Understand the differences between `var`, `const`, and `let`.
- Familiarize yourself with various data types available in JavaScript.
- Learn how to use if, if-else statements for conditional logic.
- Practice using loops (while, for) and loop control statements.
- Learn how to create and use functions.
- Understand the concept of scope for variables.
- Learn to work with objects and arrays.
- Understand how to manipulate dictionaries and arrays.
- Familiarize yourself with basic arithmetic operators.
- Learn how to import external files.
- Understand basic error handling and type conversion.

## Requirements

To successfully complete this project, make sure you follow these guidelines:

- Use an allowed text editor: vi, vim, emacs.
- All your files should end with a new line.
- The first line of each file should be exactly `#!/usr/bin/node`.
- Your code should be semistandard compliant (version 16.x.x) with semicolons.
- All your files must be executable.
- Ensure your files' length adheres to the specified limits.
- The code should be written and executed using Node.js version 14.x.
- The project directory should include a `README.md` file at the root.

## Tasks

This project consists of a series of tasks, each requiring you to write a JavaScript script to achieve a specific objective. The tasks include:

1. **First Constant, First Print**: Print a message using a constant variable.
2. **3 Languages**: Print multiple lines with different messages.
3. **Arguments**: Handle command-line arguments and print messages accordingly.
4. **Value of My Argument**: Print the value of the first command-line argument.
5. **Create a Sentence**: Concatenate and print two arguments in a specific format.
6. **Loop to Languages**: Print multiple lines using an array and a loop.
7. **I Love C**: Print a message multiple times based on a given number.
8. **Square**: Print a square pattern based on a given size.
9. **Add**: Create and use a function to add two integers.
10. **Factorial**: Compute and print the factorial of a number using recursion.
11. **Second Biggest!**: Find the second biggest integer among the arguments.
12. **Object**: Update a value within an object.
13. **Add File**: Create an external module to add two integers.
14. **Const or Not Const**: Modify a global variable using an external script.
15. **Call Me Moby**: Call a function multiple times with a specified parameter.
16. **Add Me Maybe**: Call a function that increments a value.
17. **Increment Object**: Extend an object with a function that increments a value.

## Getting Started

To get started with this project, make sure you have Node.js version 14.x installed on your machine. You can follow these steps to set up the environment:

1. Install Node.js 14.x:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

2. Install the semistandard coding style:

```bash
$ sudo npm install semistandard --global
```

3. Clone this repository:

```bash
$ git clone https://github.com/Dr-dyrane/alx-higher_level_programming.git
```

4. Navigate to the `0x12-javascript-warm_up` directory:

```bash
$ cd alx-higher_level_programming/0x12-javascript-warm_up
```

5. Follow the instructions in each task's description to complete the tasks.

6. Run your JavaScript files using Node.js:

```bash
$ node your_script.js
```

## File Descriptions

Here's a brief description of the files present in the project directory:

| File Name                    | Description                                                                                    | Implementation                                                                                                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0-javascript_is_amazing.js` | Prints the message "JavaScript is amazing".                                                    | `javascript console.log("JavaScript is amazing");`                                                                                                                                                                                                                  |
| `1-multi_languages.js`       | Prints three different messages using `console.log()`.                                         | `javascript console.log("C is fun");`<br>`console.log("Python is cool");`<br>`console.log("JavaScript is amazing");`                                                                                                                                                |
| `2-arguments.js`             | Handles command-line arguments and prints messages based on the number of arguments passed.    | `javascript if (process.argv.length === 2)`<br>`console.log("No argument");`<br>`else if (process.argv.length === 3)`<br>`console.log("Argument found");`<br>`else`<br>`console.log("Arguments found");`                                                            |
| `3-value_argument.js`        | Prints the value of the first command-line argument or "No argument" if none.                  | `javascript if (process.argv.length === 2)`<br>`console.log("No argument");`<br>`else`<br>`console.log(process.argv[2]);`                                                                                                                                           |
| `4-concat.js`                | Concatenates and prints two command-line arguments in a specific format.                       | `javascript if (process.argv.length < 3)`<br>`console.log("undefined is undefined");`<br>`else if (process.argv.length === 3)`<br>`` console.log(`${process.argv[2]} is undefined`); ``<br>`else`<br>`` console.log(`${process.argv[2]} is ${process.argv[3]}`); `` |
| `5-to_integer.js`            | Prints whether the first command-line argument can be converted to an integer or not.          | `javascript const num = parseInt(process.argv[2]);`<br>`if (isNaN(num))`<br>`console.log("Not a number");`<br>`else`<br>`` console.log(`My number: ${num}`); ``                                                                                                     |
| `6-multi_languages_loop.js`  | Prints multiple lines using an array and a loop.                                               | `javascript const languages = ['C', 'Python', 'JavaScript'];`<br>`for (const language of languages)`<br>`` console.log(`${language} is fun`); ``                                                                                                                    |
| `7-multi_c.js`               | Prints "C is fun" a given number of times.                                                     | `javascript const times = parseInt(process.argv[2]);`<br>`if (isNaN(times))`<br>`console.log("Missing number of occurrences");`<br>`else`<br>`for (let i = 0; i < times; i++)`<br>`console.log("C is fun");`                                                        |
| `8-square.js`                | Prints a square pattern based on a given size.                                                 | `javascript const size = parseInt(process.argv[2]);`<br>`if (isNaN(size))`<br>`console.log("Missing size");`<br>`else`<br>`for (let i = 0; i < size; i++)`<br>`console.log("X".repeat(size));`                                                                      |
| `9-add.js`                   | Defines a function `add` to add two integers and uses it to print the addition.                | `javascript function add(a, b) { return a + b; }`<br>`console.log(add(3, 5));`                                                                                                                                                                                      |
| `10-factorial.js`            | Defines a recursive function `factorial` to compute and print the factorial of a number.       | `javascript function factorial(num) {`<br>`if (num <= 1) return 1;`<br>`return num * factorial(num - 1);`<br>`}`<br>`console.log(factorial(5));`                                                                                                                    |
| `11-second_biggest.js`       | Finds and prints the second biggest integer among the arguments.                               | `javascript if (process.argv.length <= 3)`<br>`console.log(0);`<br>`else {`<br>`const numbers = process.argv.slice(2).map(Number);`<br>`const sortedNumbers = numbers.sort((a, b) => b - a);`<br>`console.log(sortedNumbers[1]);`<br>`}`                            |
| `12-object.js`               | Updates the value of a property in an object.                                                  | `javascript myObject.value = 89;`                                                                                                                                                                                                                                   |
| `13-add.js`                  | Defines an external module with a function to add two integers.                                | `javascript module.exports.add = function (a, b) { return a + b; }`                                                                                                                                                                                                 |
| `100-let_me_const.js`        | Modifies a global variable from an external script.                                            | `javascript myVar = 333;`                                                                                                                                                                                                                                           |
| `101-call_me_moby.js`        | Defines an external module with a function to call another function multiple times.            | `javascript module.exports.callMeMoby = function (x, theFunction) { for (let i = 0; i < x; i++) theFunction(); }`                                                                                                                                                   |
| `102-add_me_maybe.js`        | Defines an external module with a function that increments a value and calls another function. | `javascript module.exports.addMeMaybe = function (number, theFunction) { theFunction(number + 1); }`                                                                                                                                                                |
| `103-object_fct.js`          | Extends an object with a method that increments a value.                                       | `javascript myObject.incr = function () { this.value++; };`                                                                                                                                                                                                         |

## Author

This project is authored by [Alexander Udeogaranya](https://github.com/Dr-dyrane). If you have any questions or need assistance, feel free to contact me through GitHub.
