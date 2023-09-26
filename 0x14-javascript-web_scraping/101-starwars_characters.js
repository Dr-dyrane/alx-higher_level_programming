#!/usr/bin/node
const request = require('request');

/**
 * StarWarsCharacterOrderPrinter class for printing characters of a Star Wars movie in the correct order.
 */
class StarWarsCharacterOrderPrinter {
  /**
   * Create a StarWarsCharacterOrderPrinter instance.
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
   * Print all characters of the Star Wars movie in the correct order.
   */
  printCharactersInOrder () {
    // Define the Star Wars API endpoint URL
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${this.movieId}`;

    // Send a GET request to the Star Wars API
    request(apiUrl, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event StarWarsCharacterOrderPrinter#error
         * @type {Error}
         */
        console.error(error);
        process.exit(1);
      }

      if (response.statusCode === 200) {
        // Parse the JSON response
        const movieData = JSON.parse(body);

        // Fetch and print the characters in the correct order
        movieData.characters.reduce((previous, characterUrl) => {
          return previous.then(() => {
            return new Promise((resolve) => {
              request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                  /**
                   * Handle character request error.
                   *
                   * @event StarWarsCharacterOrderPrinter#error
                   * @type {Error}
                   */
                  console.error(charError);
                  process.exit(1);
                }

                if (charResponse.statusCode === 200) {
                  const characterData = JSON.parse(charBody);
                  console.log(characterData.name);
                  resolve();
                } else {
                  /**
                   * Handle character request response error.
                   *
                   * @event StarWarsCharacterOrderPrinter#error
                   * @type {Error}
                   */
                  console.error(`Error: ${charResponse.statusCode}`);
                  process.exit(1);
                }
              });
            });
          });
        }, Promise.resolve());
      } else {
        /**
         * Handle response error.
         *
         * @event StarWarsCharacterOrderPrinter#error
         * @type {Error}
         */
        console.error(`Error: ${response.statusCode}`);
        process.exit(1);
      }
    });
  }

  /**
   * Run the StarWarsCharacterOrderPrinter script.
   * Checks command-line arguments and prints characters of the specified Star Wars movie in the correct order.
   */
  static run () {
    // Check if the user provided the movie ID as an argument
    if (process.argv.length !== 3 || isNaN(Number(process.argv[2]))) {
      /**
       * Usage error.
       *
       * @event StarWarsCharacterOrderPrinter#usageError
       * @type {Error}
       */
      console.error('Usage: ./101-starwars_characters.js <movie_id>');
      process.exit(1);
    }

    // Parse the movie ID from the command line argument
    const movieId = parseInt(process.argv[2]);

    // Create an instance of StarWarsCharacterOrderPrinter and print characters in order
    const characterOrderPrinter = new StarWarsCharacterOrderPrinter(movieId);
    characterOrderPrinter.printCharactersInOrder();
  }
}

// Run the script
StarWarsCharacterOrderPrinter.run();
