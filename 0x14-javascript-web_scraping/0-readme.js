#!/usr/bin/node
const fs = require('fs');

/**
 * FileReader class for reading and printing the content of a file.
 */
class FileReader {
  /**
   * Create a FileReader instance.
   *
   * @param {string} filePath - The path to the file to be read.
   */
  constructor (filePath) {
    /**
     * The path to the file to be read.
     * @type {string}
     */
    this.filePath = filePath;
  }

  /**
   * Read and print the content of the file.
   */
  readAndPrintFileContent () {
    // Read the content of the file in utf-8 encoding
    fs.readFile(this.filePath, 'utf-8', (err, data) => {
      if (err) {
        /**
         * Handle file read error.
         *
         * @event FileReader#error
         * @type {Error}
         */
        console.error(err);
        process.exit(1);
      }

      /**
       * Content of the file.
       *
       * @event FileReader#data
       * @type {string}
       */
      console.log(data);
    });
  }

  /**
   * Run the FileReader script.
   * Checks command-line arguments and reads/prints the file content.
   */
  static run () {
    // Check if the user provided a file path as an argument
    if (process.argv.length !== 3) {
      /**
       * Usage error.
       *
       * @event FileReader#usageError
       * @type {Error}
       */
      console.error('Usage: ./0-readme.js <file_path>');
      process.exit(1);
    }

    // Get the file path from the command line argument
    const filePath = process.argv[2];

    // Create an instance of FileReader and read/print the file content
    const fileReader = new FileReader(filePath);
    fileReader.readAndPrintFileContent();
  }
}

// Run the script
FileReader.run();
