#!/usr/bin/node
const request = require('request');

/**
 * Display the status code of a GET request to a URL.
 *
 * @param {string} url - The URL to send the GET request to.
 */
function displayStatusCode (url) {
  // Send a GET request to the specified URL
  request(url, (error, response) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    } else {
      // Print the status code of the response
      console.log(`code: ${response.statusCode}`);
    }
  });
}

// Check if the user provided a URL as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Get the URL from the command line argument
const url = process.argv[2];

// Call the function to display the status code of the GET request
displayStatusCode(url);
