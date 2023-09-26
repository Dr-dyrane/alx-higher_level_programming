#!/usr/bin/node
const fs = require('fs');

/**
 * FileWriter class for writing a string to a file.
 */
class FileWriter {
  /**
   * Create a FileWriter instance.
   *
   * @param {string} filePath - The path to the file to be written.
   * @param {string} content - The string to write to the file.
   */
  constructor (filePath, content) {
    /**
     * The path to the file to be written.
     * @type {string}
     */
    this.filePath = filePath;

    /**
     * The string to write to the file.
     * @type {string}
     */
    this.content = content;
  }

  /**
   * Write the string content to the file.
   */
  writeStringToFile () {
    // Write the content to the file in utf-8 encoding
    fs.writeFile(this.filePath, this.content, 'utf-8', (err) => {
      if (err) {
        /**
         * Handle file write error.
         *
         * @event FileWriter#error
         * @type {Error}
         */
        console.error(err);
        process.exit(1);
      }
    });
  }

  /**
   * Run the FileWriter script.
   * Checks command-line arguments and writes the string to the file.
   */
  static run () {
    // Check if the user provided both a file path and content as arguments
    if (process.argv.length !== 4) {
      /**
       * Usage error.
       *
       * @event FileWriter#usageError
       * @type {Error}
       */
      console.error('Usage: ./1-writeme.js <file_path> <content>');
      process.exit(1);
    }

    // Get the file path and content from the command line arguments
    const filePath = process.argv[2];
    const content = process.argv[3];

    // Create an instance of FileWriter and write the string to the file
    const fileWriter = new FileWriter(filePath, content);
    fileWriter.writeStringToFile();
  }
}

// Run the script
FileWriter.run();
