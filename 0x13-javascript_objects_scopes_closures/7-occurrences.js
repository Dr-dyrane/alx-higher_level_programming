#!/usr/bin/node

/**
 * Returns the number of occurrences of a search element in a list.
 *
 * This function iterates through the given list and counts the occurrences
 * of the specified search element.
 *
 * @function
 * @param {Array} list - The list of elements to search through.
 * @param {*} searchElement - The element to search for in the list.
 * @returns {number} The number of occurrences of the search element.
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    count = (list[i] === searchElement ? count + 1 : count);
  }

  return count;
};
