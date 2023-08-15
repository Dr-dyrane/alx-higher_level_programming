#!/usr/bin/node

/**
 * Returns a function that converts a number from base 10 to the specified base.
 *
 * This function takes a base as an argument and returns an inner function
 * that converts a given number from base 10 to the specified base.
 *
 * @function
 * @param {number} base - The target base for conversion.
 * @returns {function} The inner function that performs the conversion.
 */
exports.converter = function (base) {
  /**
   * Converts a number from base 10 to the specified base.
   *
   * This inner function takes a number as input and returns its
   * representation in the specified base.
   *
   * @function
   * @param {number} n - The number to be converted.
   * @returns {string} The converted number in the specified base.
   */
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
