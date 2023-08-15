#!/usr/bin/node

/**
 * Adds two integers and returns the result.
 * @param {number} a - The first integer.
 * @param {number} b - The second integer.
 * @returns {number} The sum of the two integers.
 */
function add (a, b) {
  return a + b;
}

// Get the first and second command-line arguments and convert them to numbers.
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

// Calculate the sum using the add function.
const sum = add(num1, num2);

// Print the result.
console.log(sum);
