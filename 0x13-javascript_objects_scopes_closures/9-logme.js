#!/usr/bin/node

/**
 * Prints the number of arguments already printed and the new argument value.
 *
 * This function logs the current count of arguments that have been printed
 * along with the new argument value provided as input.
 *
 * @function
 * @param {any} item - The argument value to be printed.
 */
let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
