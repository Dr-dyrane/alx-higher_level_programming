#!/usr/bin/node

/**
 * Finds the second biggest integer among the list of arguments.
 * @param {number[]} args - An array of integers.
 * @returns {number} The second biggest integer, or 0 if not found.
 */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
