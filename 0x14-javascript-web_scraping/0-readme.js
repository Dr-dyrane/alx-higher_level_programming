#!/usr/bin/node
const fs = require('fs');

/**
 * Read and print the content of a file.
 *
 * @param {string} filePath - The path to the file to be read.
 */
function readAndPrintFileContent (filePath) {
  // Check if the user provided a file path as an argument
  if (process.argv.length !== 3) {
    console.error('Usage: ./0-readme.js <file_path>');
    process.exit(1);
  }

  // Read the content of the file in utf-8 encoding
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      // Print the error object if an error occurred during reading
      console.error(err);
      process.exit(1);
    }

    // Print the content of the file
    console.log(data);
  });
}

// Get the file path from the command line argument
const filePath = process.argv[2];

// Call the function to read and print the file content
readAndPrintFileContent(filePath);
