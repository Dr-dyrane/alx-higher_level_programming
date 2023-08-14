#!/usr/bin/node

/**
 * Returns the addition of two integers.
 * @param {number} a - The first integer.
 * @param {number} b - The second integer.
 * @returns {number} The sum of a and b.
 */
function add(a, b) {
    return a + b;
  }
  
  // Export the add function to make it visible from outside.
  module.exports = { add };
  