#!/usr/bin/node

/**
 * Increments a number and calls a given function.
 * @param {number} number - The number to be incremented.
 * @param {Function} theFunction - The function to be called.
 */
exports.addMeMaybe = function (number, theFunction) {
  // Increment the number by 1 before passing it to theFunction.
  theFunction(++number);
};
