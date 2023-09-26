#!/usr/bin/node
const request = require('request');

/**
 * StarWarsTitlePrinter class for printing the title of a Star Wars movie by episode number.
 */
class StarWarsTitlePrinter {
  /**
   * Create a StarWarsTitlePrinter instance.
   *
   * @param {number} episodeNumber - The episode number of the movie.
   */
  constructor (episodeNumber) {
    /**
     * The episode number of the movie.
     * @type {number}
     */
    this.episodeNumber = episodeNumber;

    /**
     * The URL for the Star Wars API with the provided episode number.
     * @type {string}
     */
    this.url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;
  }

  /**
   * Print the title of the Star Wars movie by episode number.
   */
  printStarWarsTitle () {
    // Send a GET request to the URL
    request(this.url, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event StarWarsTitlePrinter#error
         * @type {Error}
         */
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

  /**
   * Run the StarWarsTitlePrinter script.
   * Checks command-line arguments, validates the episode number, and prints the movie title.
   */
  static run () {
    // Check if the user provided an episode number as an argument
    if (process.argv.length !== 3 || isNaN(Number(process.argv[2]))) {
      /**
       * Usage error.
       *
       * @event StarWarsTitlePrinter#usageError
       * @type {Error}
       */
      console.error('Usage: ./3-starwars_title.js <episode_number>');
      process.exit(1);
    }

    // Get the episode number from the command line argument and convert it to a number
    const episodeNumber = Number(process.argv[2]);

    // Create an instance of StarWarsTitlePrinter and print the Star Wars movie title
    const titlePrinter = new StarWarsTitlePrinter(episodeNumber);
    titlePrinter.printStarWarsTitle();
  }
}

// Run the script
StarWarsTitlePrinter.run();
