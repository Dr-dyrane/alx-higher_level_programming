#!/usr/bin/node

/**
 * Script that prints a message based on the number of arguments passed.
 * @module 2-arguments
 */

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
