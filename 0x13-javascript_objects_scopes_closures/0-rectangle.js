#!/usr/bin/node

// Rectangle class definition
class Rectangle {
  // Constructor
  constructor (width, height) {
    // Initialize width and height properties
    this.width = width;
    this.height = height;
  }

  // Method to calculate and return the area of the rectangle
  calculateArea () {
    return this.width * this.height;
  }

  // Method to print the dimensions of the rectangle
  printDimensions () {
    console.log(`Width: ${this.width}, Height: ${this.height}`);
  }
}

// Create an instance of Rectangle
const r1 = new Rectangle(5, 10);

// Test the methods
console.log(`Area: ${r1.calculateArea()}`);
r1.printDimensions();

// Export the Rectangle class
module.exports = Rectangle;
