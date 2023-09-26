#!/usr/bin/node
const request = require('request');

/**
 * StarWarsCharacterCounter class for counting movies with the character "Wedge Antilles."
 */
class StarWarsCharacterCounter {
  /**
   * Create a StarWarsCharacterCounter instance.
   *
   * @param {string} apiUrl - The API URL of the Star Wars API films endpoint.
   * @param {number} characterId - The ID of the character "Wedge Antilles."
   */
  constructor (apiUrl, characterId) {
    /**
     * The API URL of the Star Wars API films endpoint.
     * @type {string}
     */
    this.apiUrl = apiUrl;

    /**
     * The ID of the character "Wedge Antilles."
     * @type {string}
     */
    this.characterId = characterId;

    /**
     * The count of movies with "Wedge Antilles."
     * @type {number}
     */
    this.count = 0;
  }

  /**
   * Count the number of movies with the character "Wedge Antilles."
   */
  countMoviesWithWedgeAntilles () {
    // Send a GET request to the provided API URL
    request.get(this.apiUrl, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event StarWarsCharacterCounter#error
         * @type {Error}
         */
        console.error(error);
        process.exit(1);
      } else {
        // Parse the JSON response
        const data = JSON.parse(body);

        // Iterate through the films and characters data
        data.results.forEach((film) => {
          film.characters.forEach((character) => {
            // Check if the character ID includes the specified ID
            if (character.includes(this.characterId)) {
              this.count += 1;
            }
          });
        });
        // Print the final count of movies with "Wedge Antilles"
        console.log(this.count);
      }
    });
  }

  /**
   * Run the StarWarsCharacterCounter script.
   * Checks command-line arguments, validates the API URL, and counts movies with "Wedge Antilles."
   */
  static run () {
    // Check if the user provided the API URL as an argument
    if (process.argv.length !== 3) {
      /**
       * Usage error.
       *
       * @event StarWarsCharacterCounter#usageError
       * @type {Error}
       */
      console.error('Usage: ./4-starwars_count.js <api_url>');
      process.exit(1);
    }

    // Define the API URL and character ID for "Wedge Antilles"
    const apiUrl = process.argv[2];
    const characterId = '18';

    // Create an instance of StarWarsCharacterCounter and count movies with "Wedge Antilles"
    const characterCounter = new StarWarsCharacterCounter(apiUrl, characterId);
    characterCounter.countMoviesWithWedgeAntilles();
  }
}

// Run the script
StarWarsCharacterCounter.run();
