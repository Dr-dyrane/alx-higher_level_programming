#!/usr/bin/node
const request = require('request');
let count = 0;

/**
 * Print the number of movies where the character "Wedge Antilles" is present.
 *
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 * @param {number} characterId - The ID of the character "Wedge Antilles."
 */
function countMoviesWithWedgeAntilles (apiUrl, characterId) {
  // Send a GET request to the provided API URL
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    } else {
      // Parse the JSON response
      const data = JSON.parse(body);

      // Iterate through the films and characters data
      data.results.forEach((film) => {
        film.characters.forEach((character) => {
          // Check if the character ID includes the specified ID
          if (character.includes(characterId)) {
            count += 1;
          }
        });
      });
      // Print the final count of movies with "Wedge Antilles"
      console.log(count);
    }
  });
}

// Check if the user provided the API URL as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

// Define the API URL and character ID for "Wedge Antilles"
const apiUrl = process.argv[2];
const characterId = '18';

// Call the function to count movies with "Wedge Antilles"
countMoviesWithWedgeAntilles(apiUrl, characterId);
