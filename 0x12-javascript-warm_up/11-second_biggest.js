#!/usr/bin/node

/**
 * Searches for the second biggest integer in the list of arguments.
 * @param {number[]} args - An array of integers.
 * @returns {number} The second biggest integer, or 0 if not found.
 */
function findSecondBiggest(args) {
  // If there are less than two arguments, return 0.
  if (args.length < 2) {
    return 0;
  }

  // Convert arguments to an array of integers and sort them in ascending order.
  const integers = args.map(Number).sort((a, b) => a - b);

  // Return the second biggest integer.
  return integers[integers.length - 2];
}

// Get the command-line arguments excluding the first two (node and script name).
const args = process.argv.slice(2);

// Find the second biggest integer among the provided arguments.
const result = findSecondBiggest(args);

// Print the result.
console.log(result);
