#!/usr/bin/node

/**
 * Script that concatenates the content of two source files into a destination file.
 * @module 102-concat
 */

const fs = require('fs');

// Get the file paths of the source files and the destination file from command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Check if the source files exist and if the destination file is provided
if (
  fs.existsSync(fileA) &&
  fs.statSync(fileA).isFile &&
  fs.existsSync(fileB) &&
  fs.statSync(fileB).isFile &&
  fileC !== undefined
) {
  // Read the content of the source files
  const fileAContent = fs.readFileSync(fileA);
  const fileBContent = fs.readFileSync(fileB);

  // Create a write stream for the destination file
  const stream = fs.createWriteStream(fileC);

  // Write the content of the source files to the destination file
  stream.write(fileAContent);
  stream.write(fileBContent);

  // Close the write stream
  stream.end();
}
