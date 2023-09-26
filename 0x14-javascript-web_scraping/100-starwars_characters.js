#!/usr/bin/node
const request = require('request');

/**
 * StarWarsCharacterPrinter class for printing characters of a Star Wars movie by movie ID.
 */
class StarWarsCharacterPrinter {
  /**
   * Create a StarWarsCharacterPrinter instance.
   *
   * @param {number} movieId - The ID of the Star Wars movie.
   */
  constructor (movieId) {
    /**
     * The ID of the Star Wars movie.
     * @type {number}
     */
    this.movieId = movieId;
  }

  /**
   * Print all characters of the Star Wars movie.
   */
  printCharactersByMovieId () {
    // Define the Star Wars API endpoint URL
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${this.movieId}`;

    // Send a GET request to the Star Wars API
    request(apiUrl, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event StarWarsCharacterPrinter#error
         * @type {Error}
         */
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
              /**
               * Handle character request error.
               *
               * @event StarWarsCharacterPrinter#error
               * @type {Error}
               */
              console.error(charError);
              process.exit(1);
            }

            if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } else {
              /**
               * Handle character request response error.
               *
               * @event StarWarsCharacterPrinter#error
               * @type {Error}
               */
              console.error(`Error: ${charResponse.statusCode}`);
              process.exit(1);
            }
          });
        });
      } else {
        /**
         * Handle response error.
         *
         * @event StarWarsCharacterPrinter#error
         * @type {Error}
         */
        console.error(`Error: ${response.statusCode}`);
        process.exit(1);
      }
    });
  }

  /**
   * Run the StarWarsCharacterPrinter script.
   * Checks command-line arguments and prints characters of the specified Star Wars movie.
   */
  static run () {
    // Check if the user provided the movie ID as an argument
    if (process.argv.length !== 3 || isNaN(Number(process.argv[2]))) {
      /**
       * Usage error.
       *
       * @event StarWarsCharacterPrinter#usageError
       * @type {Error}
       */
      console.error('Usage: ./100-starwars_characters.js <movie_id>');
      process.exit(1);
    }

    // Parse the movie ID from the command line argument
    const movieId = parseInt(process.argv[2]);

    // Create an instance of StarWarsCharacterPrinter and print characters
    const characterPrinter = new StarWarsCharacterPrinter(movieId);
    characterPrinter.printCharactersByMovieId();
  }
}

// Run the script
StarWarsCharacterPrinter.run();
