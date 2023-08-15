#!/usr/bin/node

/**
 * Script that demonstrates incrementing an integer value in an object.
 * @module 103-object_fct
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/**
 * Function to increment the integer value in the object.
 * @function incr
 */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
