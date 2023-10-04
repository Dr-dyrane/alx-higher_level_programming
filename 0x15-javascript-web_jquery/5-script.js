/**
 * ListItemAdder class to add a new <li> element to a list.
 */
class ListItemAdder {
  /**
     * Initializes the ListItemAdder class.
     */
  constructor () {
    // Wait for the document to be fully loaded before executing the script
    $(document).ready(() => {
      // Select the <div> element with ID 'add_item' using jQuery
      const addItemElement = $('#add_item');

      // Add a click event handler to add a new <li> element when clicked
      addItemElement.click(() => {
        this.addListItem();
      });
    });
  }

  /**
     * Adds a new <li> element to the list with class 'my_list'.
     */
  addListItem () {
    // Create a new <li> element with the text 'Item'
    const newItem = $('<li>Item</li>');

    // Select the <ul> element with class 'my_list' using jQuery
    const listElement = $('ul.my_list');

    // Append the new <li> element to the list
    listElement.append(newItem);
  }
}

// Create an instance of the ListItemAdder class
const listItemAdder = new ListItemAdder();
