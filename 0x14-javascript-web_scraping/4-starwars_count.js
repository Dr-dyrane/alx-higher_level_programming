#!/usr/bin/node
const request = require('request');

/**
 * Print the number of movies where the character "Wedge Antilles" is present.
 *
 * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
 * @param {number} characterId - The ID of the character "Wedge Antilles."
 */
function countMoviesWithWedgeAntilles(apiUrl, characterId) {
  // Send a GET request to the provided API URL
  request(apiUrl, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      // Parse the JSON response
      const filmsData = JSON.parse(body);

      // Count movies where "Wedge Antilles" is present
      let count = 0;
      for (const film of filmsData.results) {
        if (film.characters.includes(characterId)) {
          count += 1;
        }
      }

      // Print the number of films
      console.log(count);
    } else {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
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
