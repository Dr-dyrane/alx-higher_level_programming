#!/usr/bin/node

/**
 * Represents an object with an incrementable value property.
 * @typedef {Object} MyObject
 * @property {string} type - The type of the object.
 * @property {number} value - The current value of the object.
 * @property {Function} incr - A function to increment the value.
 */

/**
 * The main script logic.
 */
(function () {
  // Initialize myObject with an initial type and value.
  const myObject = {
    type: 'object',
    value: 12
  };

  // Print the initial state of myObject.
  console.log(myObject);

  /**
   * Increment the value property of the object.
   * @method incr
   * @memberof MyObject
   */
  myObject.incr = function () {
    this.value++;
  };

  // Call the incr() method to increment the value.
  myObject.incr();

  // Print the updated state of myObject.
  console.log(myObject);

  // Call the incr() method again to further increment the value.
  myObject.incr();

  // Print the final state of myObject after multiple increments.
  console.log(myObject);
})();
