#!/usr/bin/node
const fs = require('fs');
const request = require('request');

/**
 * Get the contents of a webpage and store it in a file.
 *
 * @param {string} url - The URL of the webpage to request.
 * @param {string} filePath - The file path to store the body response.
 */
function requestAndStoreWebpage (url, filePath) {
  // Send a GET request to the provided URL
  request(url, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      // Write the body response to the specified file
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          // Print the error object if there was an error while writing
          console.error(err);
          process.exit(1);
        }

        console.log(`Downloaded and saved to ${filePath}`);
      });
    } else {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
    }
  });
}

// Check if the user provided the URL and file path as arguments
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <url> <file_path>');
  process.exit(1);
}

// Define the URL and file path
const url = process.argv[2];
const filePath = process.argv[3];

// Call the function to request and store the webpage
requestAndStoreWebpage(url, filePath);
