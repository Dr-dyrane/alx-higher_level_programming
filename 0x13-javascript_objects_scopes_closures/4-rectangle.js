#!/usr/bin/node

/**
 * Represents a rectangle class with width, height, and manipulation methods.
 *
 * This class defines a rectangle based on the provided width and height parameters.
 * If the provided width and height are both positive integers, the attributes are initialized.
 * The class provides methods to print the rectangle, rotate its dimensions, and double its size.
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

  /**
   * Rotate the dimensions of the rectangle.
   *
   * This method exchanges the width and height of the rectangle.
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * Double the dimensions of the rectangle.
   *
   * This method multiplies the width and height of the rectangle by 2.
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
