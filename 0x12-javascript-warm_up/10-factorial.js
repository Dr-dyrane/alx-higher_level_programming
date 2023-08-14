#!/usr/bin/node

/**
 * Calculates the factorial of a given integer using recursion.
 * @param {number} n - The integer for which to calculate the factorial.
 * @returns {number} The factorial of the given integer.
 */
function factorial(n) {
  // Base case: factorial of 0 is 1.
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    // Recursive case: factorial(n) = n * factorial(n - 1)
    return n * factorial(n - 1);
  }
}

// Get the first command-line argument and convert it to a number.
const inputNumber = Number(process.argv[2]);

// Calculate the factorial of the input number using the factorial function.
const result = factorial(inputNumber);

// Print the result.
console.log(result);
