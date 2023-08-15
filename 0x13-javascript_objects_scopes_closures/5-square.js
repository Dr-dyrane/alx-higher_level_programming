#!/usr/bin/node

/**
 * Represents a square class that inherits from the rectangle class.
 *
 * This class defines a square based on the provided size parameter.
 * It inherits the behavior of the Rectangle class and uses its constructor.
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /**
   * Create a new Square instance.
   *
   * @constructor
   * @param {number} size - The size of the square's sides.
   */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
