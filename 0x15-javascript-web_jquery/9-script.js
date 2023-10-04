/**
 * TranslationFetcher class to fetch and display translations of "hello" using jQuery.
 */
class TranslationFetcher {
    /**
     * Initializes the TranslationFetcher class.
     * @param {string} apiUrl - The URL of the translation API service.
     * @param {string} outputId - The ID of the output div for displaying translations.
     */
    constructor(apiUrl, outputId) {
        this.apiUrl = apiUrl;
        this.outputDiv = $(`#${outputId}`);
        this.fetchAndDisplayTranslation();
    }

    /**
     * Fetches and displays the translation of "hello" from the API.
     */
    fetchAndDisplayTranslation() {
        // Use jQuery's getJSON method to fetch the translation
        $.getJSON(this.apiUrl, (data) => {
            // Set the text content of the output div to the translation
            this.outputDiv.text(data.hello);
        })
        .fail((error) => {
            // Handle any errors that occur during the API request
            console.error('Error fetching translation:', error);
        });
    }
}

// Create an instance of TranslationFetcher when the document is fully loaded
$(document).ready(() => {
    const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
    const outputId = 'hello';

    new TranslationFetcher(apiUrl, outputId);
});
