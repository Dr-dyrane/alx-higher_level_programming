#!/usr/bin/node
const request = require('request');

/**
 * Print the title of a Star Wars movie by its episode number.
 *
 * @param {number} episodeNumber - The episode number of the movie.
 */
function printStarWarsTitle (episodeNumber) {
  // Define the URL with the provided episode number
  const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

  // Send a GET request to the URL
  request(url, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      // Parse the JSON response
      const movieData = JSON.parse(body);

      // Print the title of the movie
      console.log(movieData.title);
    } else {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
    }
  });
}

// Check if the user provided an episode number as an argument
if (process.argv.length !== 3 || isNaN(Number(process.argv[2]))) {
  console.error('Usage: ./3-starwars_title.js <episode_number>');
  process.exit(1);
}

// Get the episode number from the command line argument and convert it to a number
const episodeNumber = Number(process.argv[2]);

// Call the function to print the Star Wars movie title
printStarWarsTitle(episodeNumber);
