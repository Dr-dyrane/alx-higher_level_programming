/**
 * HeaderColorUpdater class to update the text color of the header element to red.
 */
class HeaderColorUpdater {
  /**
     * Initializes the HeaderColorUpdater class.
     * @param {string} selector - The CSS selector for the header element.
     * @param {string} color - The color to set for the header text.
     */
  constructor (selector, color) {
    this.selector = selector; // CSS selector for the header element
    this.color = color; // Color to set for the header text
    this.header = document.querySelector(this.selector); // Get the header element
    this.updateHeaderColor(); // Call the method to update the header color
  }

  /**
     * Updates the text color of the header element.
     */
  updateHeaderColor () {
    if (this.header) {
      // If the header element exists, set its text color to the specified color
      this.header.style.color = this.color;
    } else {
      // If the header element is not found, log an error message
      console.error('Header element not found.');
    }
  }
}

// Create an instance of HeaderColorUpdater when the document is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  const selector = 'header'; // CSS selector for the header element
  const color = '#FF0000'; // Red color
  new HeaderColorUpdater(selector, color); // Initialize the header color updater
});
