# JavaScript Web Scraping Project

This project contains a collection of JavaScript scripts for web scraping and data manipulation tasks. Each script performs a specific function, and this README provides an overview of each script and its usage.

## Table of Contents

1. [Requirements](#requirements)
2. [Tasks](#Tasks)
3. [Scripts](#scripts)
    - [0. Readme](#0-readme)
    - [1. Write Me](#1-write-me)
    - [2. Status Code](#2-status-code)
    - [3. Star Wars Movie Title](#3-star-wars-movie-title)
    - [4. Star Wars Wedge Antilles](#4-star-wars-wedge-antilles)
    - [5. Loripsum](#5-loripsum)
    - [6. How Many Completed?](#6-how-many-completed)
    - [7. Who Was Playing in This Movie?](#7-who-was-playing-in-this-movie)
    - [8. Right Order](#8-right-order)
4. [How to Use](#how-to-use)
5. [License](#license)
6. [Author](#author)

## Requirements

- Node.js (version 14.x)
- `semistandard` module for code style compliance
- `request` module for making HTTP requests

You can install `semistandard` and `request` modules using npm:

```bash
sudo npm install semistandard --global
sudo npm install request --global
```

## Tasks

This project involves working with JavaScript to perform various tasks related to web scraping, making HTTP requests, and processing JSON data. Below, I'll explain each task and provide an overview of what needs to be done:

### Task 0: Readme
**Objective**: Create a script that reads and prints the content of a file.

- The script takes a file path as the first argument.
- It reads the content of the file in UTF-8.
- If an error occurs during reading, it prints the error object.

### Task 1: Write me
**Objective**: Create a script that writes a string to a file.

- The script takes two arguments: a file path and a string to write.
- It writes the provided string to the specified file in UTF-8.
- If an error occurs during writing, it prints the error object.

### Task 2: Status code
**Objective**: Create a script that displays the status code of a GET request.

- The script takes a URL as the first argument.
- It makes a GET request to the specified URL using the request module.
- It prints the status code of the response.

### Task 3: Star wars movie title
**Objective**: Create a script that prints the title of a Star Wars movie based on the episode number.

- The script takes a movie ID as the first argument.
- It fetches the movie title from the Star Wars API using the provided movie ID.
- It prints the movie title.

### Task 4: Star wars Wedge Antilles
**Objective**: Create a script that prints the number of movies where the character "Wedge Antilles" is present.

- The script makes a GET request to the Star Wars API to fetch movie data.
- It filters the movies to count how many times the character "Wedge Antilles" appears.
- It prints the count.

### Task 5: Loripsum
**Objective**: Create a script that gets the contents of a webpage and stores it in a file.

- The script takes a URL to request as the first argument.
- It makes an HTTP request to the specified URL.
- It stores the response body in a file specified by the second argument.
- The file must be UTF-8 encoded.

### Task 6: How many completed?
**Objective**: Create a script that computes the number of tasks completed by user ID.

- The script takes an API URL as the first argument.
- It makes a GET request to the specified URL to fetch task data.
- It counts the number of completed tasks for each user and prints the result in JSON format.

### Task 7: Who was playing in this movie?
**Objective**: Create a script that prints all characters of a Star Wars movie based on the movie ID.

- The script takes a movie ID as the first argument.
- It fetches the list of characters from the Star Wars API for the specified movie.
- It prints each character name on a separate line.

### Task 8: Right order (Advanced)
**Objective**: Create a script that prints all characters of a Star Wars movie in the same order as the list "characters" in the /films/ response.

- The script takes a movie ID as the first argument.
- It fetches the list of characters from the Star Wars API for the specified movie.
- It prints each character name on a separate line, following the order from the API response.

For each task, you will be using the request module to make HTTP requests and fetch data. Make sure to install and use Node.js (version 14.x) for executing your scripts. You should also follow coding standards (semistandard) and ensure that your code is well-documented.

Remember to create a README.md file in the project directory to provide additional information about your scripts and how to run them.

## Scripts

### 0. Readme

This script reads and prints the content of a file. It takes the file path as an argument and reads the file in UTF-8 encoding. If any errors occur during reading, it prints the error object.

Usage:

```bash
./0-readme.js file_path
```

### 1. Write Me

This script writes a string to a file. It takes the file path and the string to write as arguments and writes the content in UTF-8 encoding. If any errors occur during writing, it prints the error object.

Usage:

```bash
./1-writeme.js file_path "string to write"
```

### 2. Status Code

This script displays the status code of a GET request to a given URL. It takes the URL as an argument and uses the `request` module to make the GET request.

Usage:

```bash
./2-statuscode.js URL
```

### 3. Star Wars Movie Title

This script prints the title of a Star Wars movie where the episode number matches a given integer. It takes the movie ID as an argument and uses the Star Wars API to fetch movie details.

Usage:

```bash
./3-starwars_title.js movie_ID
```

### 4. Star Wars Wedge Antilles

This script prints the number of movies where the character "Wedge Antilles" is present. It uses the Star Wars API and filters the result for the character ID 18.

Usage:

```bash
./4-starwars_count.js API_URL
```

### 5. Loripsum

This script gets the contents of a webpage and stores it in a file. It takes the URL to request and the file path to store the response. The file is UTF-8 encoded.

Usage:

```bash
./5-request_store.js URL file_path
```

### 6. How Many Completed?

This script computes the number of tasks completed by user ID. It takes the API URL as an argument and prints the number of completed tasks for each user.

Usage:

```bash
./6-completed_tasks.js API_URL
```

### 7. Who Was Playing in This Movie? (Advanced)

This script prints all characters of a Star Wars movie. It takes the movie ID as an argument and displays one character name per line using the Star Wars API.

Usage:

```bash
./100-starwars_characters.js movie_ID
```

### 8. Right Order (Advanced)

This script prints all characters of a Star Wars movie in the same order as the list "characters" in the /films/ response. It takes the movie ID as an argument and uses the Star Wars API.

Usage:

```bash
./101-starwars_characters.js movie_ID
```

## How to Use

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Dr-dyrane/alx-higher_level_programming.git
cd alx-higher_level_programming/0x14-javascript-web_scraping
```

2. Navigate to the directory of the script you want to run.

3. Run the script with the appropriate arguments as described in the script's usage section.

4. Follow the output to see the result of the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Alexander Udeogaranya](https://github.com/Dr-dyrane/alx-higher_level_programming/tree/master/0x14-javascript-web_scraping)