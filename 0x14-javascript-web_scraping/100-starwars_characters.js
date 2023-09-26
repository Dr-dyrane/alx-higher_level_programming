#!/usr/bin/node
const request = require('request');

/**
 * Prints all characters of a Star Wars movie by movie ID.
 *
 * @param {number} movieId - The ID of the Star Wars movie.
 */
function getCharactersByMovieId (movieId) {
  // Define the Star Wars API endpoint URL
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  // Send a GET request to the Star Wars API
  request(apiUrl, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      // Parse the JSON response
      const movieData = JSON.parse(body);

      // Print the characters of the movie one by one
      movieData.characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            // Print the error object if there was an error with character request
            console.error(charError);
            process.exit(1);
          }

          if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.error(`Error: ${charResponse.statusCode}`);
            process.exit(1);
          }
        });
      });
    } else {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
    }
  });
}

// Check if the user provided the movie ID as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Parse the movie ID from the command line argument
const movieId = parseInt(process.argv[2]);

// Call the function to get characters by movie ID
getCharactersByMovieId(movieId);
