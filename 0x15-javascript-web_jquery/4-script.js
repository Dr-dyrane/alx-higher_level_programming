/**
 * HeaderClassToggler class to toggle the class of the header element.
 */
class HeaderClassToggler {
    /**
     * Initializes the HeaderClassToggler class.
     */
    constructor() {
      // Wait for the document to be fully loaded before executing the script
      $(document).ready(() => {
        // Select the <div> element with ID 'toggle_header' using jQuery
        const toggleHeaderElement = $('#toggle_header');
  
        // Select the <header> element using jQuery
        const headerElement = $('header');
  
        // Add a click event handler to toggle the class of the header element
        toggleHeaderElement.click(() => {
          // Toggle the class of the header element between 'red' and 'green'
          this.toggleHeaderClass(headerElement);
        });
      });
    }
  
    /**
     * Toggles the class of the specified element between 'red' and 'green'.
     * @param {jQuery} element - The jQuery element to toggle the class for.
     */
    toggleHeaderClass(element) {
      // Use jQuery's .toggleClass() method to toggle the class
      element.toggleClass('red green');
    }
  }
  
  // Create an instance of the HeaderClassToggler class
  const headerClassToggler = new HeaderClassToggler();
  