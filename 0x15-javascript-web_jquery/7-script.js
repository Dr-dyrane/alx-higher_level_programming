/**
 * StarWarsCharacter class to fetch and display a character's name from the Star Wars API using jQuery.
 */
class StarWarsCharacter {
  /**
     * Initializes the StarWarsCharacter class.
     */
  constructor () {
    // Define the URL of the Star Wars API endpoint
    this.apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    // Wait for the document to be fully loaded before executing the script
    $(document).ready(() => {
      // Fetch the character data from the API and display the name
      this.fetchCharacterName();
    });
  }

  /**
     * Fetches the character data from the Star Wars API and displays the name.
     */
  fetchCharacterName () {
    // Use jQuery's AJAX method to make a GET request to the API
    $.ajax({
      url: this.apiUrl,
      method: 'GET',
      dataType: 'json',
      success: (data) => {
        // Select the <div> element with ID 'character' and set its text to the character's name
        $('#character').text(data.name);
      },
      error: (error) => {
        // Handle any errors that occur during the API request
        console.error('Error fetching character data:', error);
      }
    });
  }
}

// Create an instance of the StarWarsCharacter class
const starWarsCharacter = new StarWarsCharacter();
