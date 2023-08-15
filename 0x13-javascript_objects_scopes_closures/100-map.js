#!/usr/bin/node

/**
 * Script that computes a new array by multiplying each value of the imported list by its index.
 * @module 100-map
 */

// Import the list from the file 100-data.js
const list = require('./100-data.js').list;

/**
 * Computes a new array by multiplying each value of the list by its index.
 * @param {number} val - The value from the list.
 * @param {number} idx - The index of the value in the list.
 * @returns {number} - The product of val and idx.
 */
const computeNewValue = (val, idx) => val * idx;

// Use the map function to create the new list
const newList = list.map(computeNewValue);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
