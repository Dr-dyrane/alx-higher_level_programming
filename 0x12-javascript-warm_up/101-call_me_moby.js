#!/usr/bin/node

/**
 * Executes a given function x times.
 * @param {number} x - The number of times to execute the function.
 * @param {Function} theFunction - The function to be executed.
 */
exports.callMeMoby = function (x, theFunction) {
  // Loop x times and call the given function in each iteration.
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
