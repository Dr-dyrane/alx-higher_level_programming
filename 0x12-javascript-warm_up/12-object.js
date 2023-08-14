#!/usr/bin/node

/**
 * An example object with a 'type' property and an initial 'value'.
 * @typedef {Object} MyObject
 * @property {string} type - The type of the object.
 * @property {number} value - The value associated with the object.
 */

/**
 * Initial object with type 'object' and value '12'.
 * @type {MyObject}
 */
const myObject = {
  type: 'object',
  value: 12
};

// Display the original object.
console.log(myObject);

// Modify the value property to 89.
myObject.value = 89;

// Display the object after modification.
console.log(myObject);
