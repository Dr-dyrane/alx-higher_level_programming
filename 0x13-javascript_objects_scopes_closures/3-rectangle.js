#!/usr/bin/node

/**
 * Represents a rectangle class with width, height, and printing functionality.
 *
 * This class defines a rectangle based on the provided width and height parameters.
 * If the provided width and height are both positive integers, the attributes are initialized.
 * The class also provides a method, `print()`, that prints a visual representation of the rectangle using the character 'X'.
 */
class Rectangle {
  /**
   * Create a new Rectangle instance.
   *
   * @constructor
   * @param {number} w - The width of the rectangle.
   * @param {number} h - The height of the rectangle.
   */
  constructor (w, h) {
    /**
     * The width of the rectangle.
     * @type {number}
     */
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      /**
       * The height of the rectangle.
       * @type {number}
       */
      this.height = h;
    }
  }

  /**
   * Print a visual representation of the rectangle.
   *
   * This method prints the rectangle using the character 'X'.
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Rectangle;
