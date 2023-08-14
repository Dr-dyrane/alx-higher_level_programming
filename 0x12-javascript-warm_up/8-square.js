#!/usr/bin/node

/**
 * Prints a square of given size using 'X' characters.
 * @param {number} size - The size of the square.
 */
function printSquare (size) {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) {
      row += 'X';
    }
    console.log(row);
  }
}

// Get the size argument from the command-line.
const size = Math.floor(Number(process.argv[2]));

// Check if the provided size is a valid number.
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // Call the function to print the square.
  printSquare(size);
}
