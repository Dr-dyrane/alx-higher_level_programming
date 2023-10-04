/**
 * HeaderClassToggler class to toggle the 'red' class on header click.
 */
class HeaderClassToggler {
    /**
     * Initializes the HeaderClassToggler class.
     */
    constructor() {
      // Wait for the document to be fully loaded before executing the script
      $(document).ready(() => {
        // Select the <div> element with ID 'red_header' using jQuery
        const redHeaderElement = $('#red_header');
  
        // Add a click event handler to toggle the 'red' class on header click
        redHeaderElement.click(() => {
          // Select the <header> element using jQuery
          const headerElement = $('header');
  
          // Toggle the 'red' class on the <header> element
          this.toggleRedClass(headerElement);
        });
      });
    }
  
    /**
     * Toggles the 'red' class on the specified element.
     * @param {jQuery} element - The jQuery element to toggle the 'red' class for.
     */
    toggleRedClass(element) {
      // Use jQuery's .toggleClass() method to toggle the 'red' class
      element.toggleClass('red');
    }
  }
  
  // Create an instance of the HeaderClassToggler class
  const headerClassToggler = new HeaderClassToggler();
  