/**
 * ListManager class to manage a list of items using jQuery.
 */
class ListManager {
    /**
     * Create a ListManager.
     * @param {string} addButtonId - The ID of the "Add item" button.
     * @param {string} removeButtonId - The ID of the "Remove item" button.
     * @param {string} clearButtonId - The ID of the "Clear list" button.
     * @param {string} listClass - The class name of the HTML ul element.
     */
    constructor(addButtonId, removeButtonId, clearButtonId, listClass) {
        this.addButton = $(`#${addButtonId}`);
        this.removeButton = $(`#${removeButtonId}`);
        this.clearButton = $(`#${clearButtonId}`);
        this.list = $(`.${listClass}`);

        this.addItem = this.addItem.bind(this);
        this.removeItem = this.removeItem.bind(this);
        this.clearList = this.clearList.bind(this);

        this.setupEventListeners();
    }

    /**
     * Adds a new <li> element with the text "Item" to the list.
     */
    addItem() {
        const newItem = $('<li>Item</li>');
        this.list.append(newItem);
    }

    /**
     * Removes the last <li> element from the list.
     */
    removeItem() {
        this.list.find('li:last-child').remove();
    }

    /**
     * Clears all elements from the list.
     */
    clearList() {
        this.list.empty();
    }

    /**
     * Sets up event listeners for the buttons.
     */
    setupEventListeners() {
        this.addButton.click(this.addItem);
        this.removeButton.click(this.removeItem);
        this.clearButton.click(this.clearList);
    }
}

// Create a new instance of ListManager when the document is ready
$(document).ready(() => {
    const addButtonId = 'add_item';
    const removeButtonId = 'remove_item';
    const clearButtonId = 'clear_list';
    const listClass = 'my_list';

    new ListManager(addButtonId, removeButtonId, clearButtonId, listClass);
});
