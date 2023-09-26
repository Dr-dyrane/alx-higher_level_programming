#!/usr/bin/node
const fs = require('fs');

/**
 * Write a string to a file.
 *
 * @param {string} filePath - The path to the file to be written.
 * @param {string} content - The string to write to the file.
 */
function writeStringToFile (filePath, content) {
  // Write the content to the file in utf-8 encoding
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      // Print the error object if an error occurred during writing
      console.error(err);
      process.exit(1);
    }
  });
}

// Check if the user provided both a file path and content as arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <content>');
  process.exit(1);
}

// Get the file path and content from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Call the function to write the string to the file
writeStringToFile(filePath, content);
