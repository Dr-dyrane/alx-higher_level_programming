#!/usr/bin/node
/**
 * Represents a rectangle with width and height attributes.
 *
 * This class provides a blueprint for creating rectangle objects with specified width and height values.
 *
 * @class
 */
class Rectangle {
  /**
   * Creates a new Rectangle instance.
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
    this.width = w;

    /**
     * The height of the rectangle.
     * @type {number}
     */
    this.height = h;
  }
}

module.exports = Rectangle;
