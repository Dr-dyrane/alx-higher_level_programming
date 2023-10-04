/**
 * HeaderTextColorUpdater class to update header text color to red.
 */
class HeaderTextColorUpdater {
  /**
     * Initializes the HeaderTextColorUpdater class.
     */
  constructor () {
    // Wait for the document to be fully loaded before executing the script
    $(document).ready(() => {
      // Select the <header> element using jQuery
      const headerElement = $('header');

      // Update the text color of the <header> element to red (#FF0000)
      this.updateHeaderTextColor(headerElement);
    });
  }

  /**
     * Updates the text color of the specified element to red (#FF0000).
     * @param {jQuery} element - The jQuery element to update the text color for.
     */
  updateHeaderTextColor (element) {
    // Use jQuery's .css() method to change the text color to red (#FF0000)
    element.css('color', '#FF0000');
  }
}

// Create an instance of the HeaderTextColorUpdater class
const headerTextColorUpdater = new HeaderTextColorUpdater();
