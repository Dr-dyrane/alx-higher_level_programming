/**
 * StarWarsMovies class to fetch and list Star Wars movie titles using jQuery.
 */
class StarWarsMovies {
    /**
     * Initializes the StarWarsMovies class.
     * @param {string} apiUrl - The URL of the Star Wars movies API service.
     * @param {string} listId - The ID of the HTML ul element to display the movie titles.
     */
    constructor(apiUrl, listId) {
        this.apiUrl = apiUrl;
        this.list = $(`#${listId}`);
        this.fetchAndDisplayMovies();
    }

    /**
     * Fetches and displays the titles of Star Wars movies.
     */
    fetchAndDisplayMovies() {
        // Use jQuery's getJSON method to fetch the movies
        $.getJSON(this.apiUrl, (data) => {
            // Loop through the results and append each movie title to the list
            data.results.forEach((movie) => {
                const listItem = `<li>${movie.title}</li>`;
                this.list.append(listItem);
            });
        })
        .fail((error) => {
            // Handle any errors that occur during the API request
            console.error('Error fetching movies:', error);
        });
    }
}

// Create an instance of StarWarsMovies when the document is fully loaded
$(document).ready(() => {
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    const listId = 'list_movies';

    new StarWarsMovies(apiUrl, listId);
});
