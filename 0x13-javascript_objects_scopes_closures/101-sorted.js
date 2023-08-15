#!/usr/bin/node

/**
 * Script that computes a dictionary of user ids by occurrence from a given dictionary of occurrences by user id.
 * @module 101-sorted
 */

// Import the dictionary of occurrences by user id from the file 101-data.js
const dict = require('./101-data.js').dict;

// Create a new dictionary for user ids by occurrence
const newDict = {};

// Iterate through the properties of the dictionary
Object.getOwnPropertyNames(dict).forEach(occurrences => {
  // If the occurrence value is not present in the new dictionary, create a new entry
  if (newDict[dict[occurrences]] === undefined) {
    newDict[dict[occurrences]] = [occurrences];
  } else {
    // If the occurrence value is already present, append the user id to the existing entry
    newDict[dict[occurrences]].push(occurrences);
  }
});

// Print the new dictionary
console.log(newDict);
