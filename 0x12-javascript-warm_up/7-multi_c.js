#!/usr/bin/node

/**
 * Script that prints "C is fun" x times.
 * @module 7-multi_c
 * @param {number} x - The number of times to print the statement.
 */

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
