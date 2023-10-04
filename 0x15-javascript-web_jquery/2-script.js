/**
 * HeaderColorChanger class to change header text color on click.
 */
class HeaderColorChanger {
    /**
     * Initializes the HeaderColorChanger class.
     */
    constructor() {
      // Wait for the document to be fully loaded before executing the script
      $(document).ready(() => {
        // Select the <div> element with ID 'red_header' using jQuery
        const redHeaderElement = $('#red_header');
  
        // Add a click event handler to change the header text color on click
        redHeaderElement.click(() => {
          // Select the <header> element using jQuery
          const headerElement = $('header');
  
          // Update the text color of the <header> element to red (#FF0000)
          this.updateHeaderTextColor(headerElement);
        });
      });
    }
  
    /**
     * Updates the text color of the specified element to red (#FF0000).
     * @param {jQuery} element - The jQuery element to update the text color for.
     */
    updateHeaderTextColor(element) {
      // Use jQuery's .css() method to change the text color to red (#FF0000)
      element.css('color', '#FF0000');
    }
  }
  
  // Create an instance of the HeaderColorChanger class
  const headerColorChanger = new HeaderColorChanger();
  