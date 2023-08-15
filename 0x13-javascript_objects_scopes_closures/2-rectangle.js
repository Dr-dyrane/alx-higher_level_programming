#!/usr/bin/node

/**
 * Represents a rectangle class with width and height attributes.
 *
 * This class defines a rectangle based on the provided width and height parameters.
 * If the provided width and height are both positive integers, the attributes are initialized.
 * Otherwise, an empty object is created.
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
}

module.exports = Rectangle;
