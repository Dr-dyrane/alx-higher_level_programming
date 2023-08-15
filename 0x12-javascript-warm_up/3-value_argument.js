#!/usr/bin/node

/**
 * Script that prints the first argument passed to it.
 * @module 3-value_argument
 */

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
