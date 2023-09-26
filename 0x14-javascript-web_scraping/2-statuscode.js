#!/usr/bin/node
const request = require('request');

/**
 * StatusCodeFetcher class for displaying the status code of a GET request to a URL.
 */
class StatusCodeFetcher {
  /**
   * Create a StatusCodeFetcher instance.
   *
   * @param {string} url - The URL to send the GET request to.
   */
  constructor (url) {
    /**
     * The URL to send the GET request to.
     * @type {string}
     */
    this.url = url;
  }

  /**
   * Display the status code of the GET request.
   */
  displayStatusCode () {
    // Send a GET request to the specified URL
    request(this.url, (error, response) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event StatusCodeFetcher#error
         * @type {Error}
         */
        console.error(error);
        process.exit(1);
      } else {
        // Print the status code of the response
        console.log(`code: ${response.statusCode}`);
      }
    });
  }

  /**
   * Run the StatusCodeFetcher script.
   * Checks command-line arguments and displays the status code of the GET request.
   */
  static run () {
    // Check if the user provided a URL as an argument
    if (process.argv.length !== 3) {
      /**
       * Usage error.
       *
       * @event StatusCodeFetcher#usageError
       * @type {Error}
       */
      console.error('Usage: ./2-statuscode.js <URL>');
      process.exit(1);
    }

    // Get the URL from the command line argument
    const url = process.argv[2];

    // Create an instance of StatusCodeFetcher and display the status code
    const statusCodeFetcher = new StatusCodeFetcher(url);
    statusCodeFetcher.displayStatusCode();
  }
}

// Run the script
StatusCodeFetcher.run();
