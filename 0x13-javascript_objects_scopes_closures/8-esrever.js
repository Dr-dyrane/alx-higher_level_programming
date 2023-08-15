#!/usr/bin/node

/**
 * Returns the reversed version of a list.
 *
 * This function creates a new list containing the elements of the input list
 * in reverse order.
 *
 * @function
 * @param {Array} list - The list of elements to be reversed.
 * @returns {Array} A new list with elements in reverse order.
 */
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};
