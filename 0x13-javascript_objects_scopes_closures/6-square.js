#!/usr/bin/node

/**
 * Represents a square class that inherits from the previous square class.
 *
 * This class extends the behavior of the previous Square class and adds an
 * instance method charPrint(c) that prints the square using the character c.
 * If c is undefined, it uses the character X by default.
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  /**
   * Print the square using the specified character.
   *
   * @method
   * @param {string} c - The character to be used for printing.
   */
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
