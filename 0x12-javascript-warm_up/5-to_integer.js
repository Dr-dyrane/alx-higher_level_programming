#!/usr/bin/node

/**
 * Script that prints "My number: <first argument converted to integer>" if the first argument can be converted to an integer.
 * @module 5-to_integer
 */

const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
