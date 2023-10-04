/**
 * TranslationFetcher class to fetch and display translations of "Hello" using jQuery.
 */
class TranslationFetcher {
  /**
     * Initializes the TranslationFetcher class.
     * @param {string} inputId - The ID of the language code input field.
     * @param {string} buttonId - The ID of the translation button.
     * @param {string} outputId - The ID of the output div for displaying translations.
     * @param {string} apiUrl - The URL of the translation API service.
     */
  constructor (inputId, buttonId, outputId, apiUrl) {
    this.inputField = $(`#${inputId}`);
    this.translateButton = $(`#${buttonId}`);
    this.outputDiv = $(`#${outputId}`);
    this.apiUrl = apiUrl;

    this.translateButton.on('click', this.fetchAndDisplayTranslation.bind(this));
  }

  /**
     * Fetches and displays the translation of "Hello" based on the language code.
     */
  fetchAndDisplayTranslation () {
    const languageCode = this.inputField.val();
    const url = `${this.apiUrl}?lang=${languageCode}`;

    $.getJSON(url)
      .done(data => {
        this.outputDiv.text(data.hello);
      })
      .fail(() => {
        this.outputDiv.text('Translation not found');
      });
  }
}

// Create an instance of TranslationFetcher when the document is fully loaded
$(document).ready(() => {
  const inputId = 'language_code';
  const buttonId = 'btn_translate';
  const outputId = 'hello';
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

  new TranslationFetcher(inputId, buttonId, outputId, apiUrl);
});
