/**
 * Class to change the text color of the <header> element.
 */
class HeaderColorChanger {
  /**
     * Creates a new HeaderColorChanger instance.
     * @param {string} selector - The CSS selector to select the HTML tag.
     * @param {string} color - The color value to set (e.g., "#FF0000" for red).
     */
  constructor (selector, color) {
    this.selector = selector;
    this.color = color;
  }

  /**
     * Changes the text color of the <header> element to the specified color.
     */
  changeColor () {
    // Select the HTML tag using the provided CSS selector
    const header = document.querySelector(this.selector);

    // Check if the header element is found
    if (header) {
      // Update the text color of the header element
      header.style.color = this.color;
    } else {
      console.error(`Element with selector '${this.selector}' not found.`);
    }
  }
}

// Create a new instance of HeaderColorChanger and change the header text color to red
const headerChanger = new HeaderColorChanger('header', '#FF0000');
headerChanger.changeColor();
