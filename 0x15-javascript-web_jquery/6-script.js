/**
 * HeaderTextUpdater class to update the text of the <header> element using jQuery.
 */
class HeaderTextUpdater {
    /**
     * Initializes the HeaderTextUpdater class.
     */
    constructor() {
      // Wait for the document to be fully loaded before executing the script
      $(document).ready(() => {
        // Select the <div> element with ID 'update_header' using jQuery
        const updateHeaderElement = $('#update_header');
  
        // Add a click event handler to update the header text when clicked
        updateHeaderElement.click(() => {
          this.updateHeaderText();
        });
      });
    }
  
    /**
     * Updates the text of the <header> element to 'New Header!!!' using jQuery.
     */
    updateHeaderText() {
      // Select the <header> element using jQuery and update its text
      $('header').text('New Header!!!');
    }
  }
  
  // Create an instance of the HeaderTextUpdater class
  const headerTextUpdater = new HeaderTextUpdater();
  