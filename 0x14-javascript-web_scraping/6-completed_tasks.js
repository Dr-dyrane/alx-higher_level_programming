#!/usr/bin/node
const request = require('request');

/**
 * TaskCounter class for computing the number of tasks completed by user ID.
 */
class TaskCounter {
  /**
   * Create a TaskCounter instance.
   *
   * @param {string} apiUrl - The API URL to fetch the tasks.
   */
  constructor (apiUrl) {
    /**
     * The API URL to fetch the tasks.
     * @type {string}
     */
    this.apiUrl = apiUrl;
  }

  /**
   * Compute and print the number of completed tasks by user ID.
   */
  countCompletedTasks () {
    // Send a GET request to the provided API URL
    request(this.apiUrl, (error, response, body) => {
      if (error) {
        /**
         * Handle request error.
         *
         * @event TaskCounter#error
         * @type {Error}
         */
        console.error(error);
        process.exit(1);
      }

      if (response.statusCode === 200) {
        // Parse the JSON response
        const tasks = JSON.parse(body);

        // Create an object to store the count of completed tasks for each user
        const completedTasksByUser = {};

        // Loop through the tasks to count completed tasks by user ID
        tasks.forEach((task) => {
          if (task.completed) {
            if (completedTasksByUser[task.userId] === undefined) {
              completedTasksByUser[task.userId] = 1;
            } else {
              completedTasksByUser[task.userId]++;
            }
          }
        });

        // Print the completed tasks count by user ID
        console.log(completedTasksByUser);
      } else {
        /**
         * Handle response error.
         *
         * @event TaskCounter#error
         * @type {Error}
         */
        console.error(`Error: ${response.statusCode}`);
        process.exit(1);
      }
    });
  }

  /**
   * Run the TaskCounter script.
   * Checks command-line arguments and computes the number of completed tasks.
   */
  static run () {
    // Check if the user provided the API URL as an argument
    if (process.argv.length !== 3) {
      /**
       * Usage error.
       *
       * @event TaskCounter#usageError
       * @type {Error}
       */
      console.error('Usage: ./6-completed_tasks.js <api_url>');
      process.exit(1);
    }

    // Define the API URL
    const apiUrl = process.argv[2];

    // Create an instance of TaskCounter and count completed tasks
    const taskCounter = new TaskCounter(apiUrl);
    taskCounter.countCompletedTasks();
  }
}

// Run the script
TaskCounter.run();
