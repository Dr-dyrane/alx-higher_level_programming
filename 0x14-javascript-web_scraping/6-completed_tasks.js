#!/usr/bin/node
const request = require('request');

/**
 * Computes the number of tasks completed by user id.
 *
 * @param {string} apiUrl - The API URL to fetch the tasks.
 */
function countCompletedTasks (apiUrl) {
  // Send a GET request to the provided API URL
  request(apiUrl, (error, response, body) => {
    if (error) {
      // Print the error object if there was an error with the request
      console.error(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      // Parse the JSON response
      const tasks = JSON.parse(body);

      // Create an object to store the count of completed tasks for each user
      const completedTasksByUser = {};

      // Loop through the tasks to count completed tasks by user id
      tasks.forEach((task) => {
        if (task.completed) {
          if (completedTasksByUser[task.userId] === undefined) {
            completedTasksByUser[task.userId] = 1;
          } else {
            completedTasksByUser[task.userId]++;
          }
        }
      });

      // Print the completed tasks count by user id
      console.log(completedTasksByUser);
    } else {
      console.error(`Error: ${response.statusCode}`);
      process.exit(1);
    }
  });
}

// Check if the user provided the API URL as an argument
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

// Define the API URL
const apiUrl = process.argv[2];

// Call the function to count completed tasks
countCompletedTasks(apiUrl);
