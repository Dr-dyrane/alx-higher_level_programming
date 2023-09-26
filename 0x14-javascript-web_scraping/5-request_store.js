#!/usr/bin/node
const request = require('request');
const fs = require('fs');

/**
 * WebpageDownloader class for getting and storing the contents of a webpage.
 */
class WebpageDownloader {
  /**
   * Create a WebpageDownloader instance.
   *
   * @param {string} url - The URL of the webpage to request.
   * @param {string} file - The file path to store the body response.
   */
  constructor (url, file) {
    /**
     * The URL of the webpage to request.
     * @type {string}
     */
    this.url = url;

    /**
     * The file path to store the body response.
     * @type {string}
     */
    this.file = file;
  }

  /**
   * Request and store the webpage content in a file.
   */
  requestAndStoreWebpage () {
    // Send a GET request to the provided URL
    request(this.url, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event WebpageDownloader#error
         * @type {Error}
         */
        console.error(error);
        process.exit(1);
      } else {
        // Write the body response to the specified file
        fs.writeFile(this.file, body, 'utf8', (err) => {
          if (err) {
            /**
             * Handle write file error.
             *
             * @event WebpageDownloader#error
             * @type {Error}
             */
            console.error(err);
            process.exit(1);
          }
          // console.log(`Downloaded and saved to ${this.file}`);
        });
      }
    });
  }

  /**
   * Run the WebpageDownloader script.
   * Checks command-line arguments, validates the URL and file path, and downloads the webpage content.
   */
  static run () {
    // Check if the user provided the URL and file path as arguments
    if (process.argv.length !== 4) {
      /**
       * Usage error.
       *
       * @event WebpageDownloader#usageError
       * @type {Error}
       */
      console.error('Usage: ./5-request_store.js <url> <file_path>');
      process.exit(1);
    }

    // Define the URL and file path
    const url = process.argv[2];
    const file = process.argv[3];

    // Create an instance of WebpageDownloader and request the webpage content
    const downloader = new WebpageDownloader(url, file);
    downloader.requestAndStoreWebpage();
  }
}

// Run the script
WebpageDownloader.run();
