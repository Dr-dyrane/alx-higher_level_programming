# JavaScript - Web jQuery

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Manual QA Review](#manual-qa-review)
- [Tasks](#tasks)
  - [Task 0: No JQuery](#task-0-no-jquery)
  - [Task 1: With JQuery](#task-1-with-jquery)
  - [Task 2: Click and Turn Red](#task-2-click-and-turn-red)
  - [Task 3: Add `.red` Class](#task-3-add-red-class)
  - [Task 4: Toggle Classes](#task-4-toggle-classes)
  - [Task 5: List of Elements](#task-5-list-of-elements)
  - [Task 6: Change the Text](#task-6-change-the-text)
  - [Task 7: Star Wars Character](#task-7-star-wars-character)
  - [Task 8: Star Wars Movies](#task-8-star-wars-movies)
  - [Task 9: Say Hello!](#task-9-say-hello)
  - [Task 10: No jQuery - Document Loaded](#task-10-no-jquery-document-loaded)
  - [Task 11: List, Add, Remove](#task-11-list-add-remove)
  - [Task 12: Say Hello to Everybody!](#task-12-say-hello-to-everybody)
  - [Task 13: And Press ENTER](#task-13-and-press-enter)

---

## Description

This project focuses on using JavaScript and jQuery to manipulate the DOM (Document Object Model) in a web page. It includes a series of tasks that involve updating elements on a webpage dynamically, making API requests, and handling user interactions.

## Concepts

- JavaScript in the browser
- Dealing with data statically versus dynamically

## Resources

Before starting this project, it's recommended to read or watch the following resources:

- [What is JavaScript?](https://intranet.alxswe.com/rltoken/NJ5XM_fzjlBKERHTkdF-uA)
- [Selector](https://intranet.alxswe.com/rltoken/wsnVUxEcAzzlCx6ES1qc7g)
- [Get and set content](https://intranet.alxswe.com/rltoken/rwtc96sn2_LHToBAd0MIhQ)
- [Manipulate CSS classes](https://intranet.alxswe.com/rltoken/IcM5kKVzssU0ibdUo-2gKQ)
- [Manipulate DOM elements](https://intranet.alxswe.com/rltoken/ve8UKsZLVw2t27PtWscZfQ)
- [API Introduction](https://intranet.alxswe.com/rltoken/vKc7XmiHG7HIh3N0Kl_VQw)
- [GET & POST request](https://intranet.alxswe.com/rltoken/Mbe7uoy0iMAfTVs2Tn4Pzg)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw)
- [What went wrong? Troubleshooting JavaScript](https://intranet.alxswe.com/rltoken/4eYyJr72PO-cohImk93M3w)
- [JQuery](https://intranet.alxswe.com/rltoken/HnjBq6jf84S9S-C15Qi0vw)
- [JQuery API](https://intranet.alxswe.com/rltoken/jvibhq-8VEdQHNUWKTCI7w)
- [JQuery Ajax](https://intranet.alxswe.com/rltoken/rBZyrXxuRuISDfPBzO9Y7Q)

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- Why jQuery makes front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with jQuery
- What are the differences between ID, class, and tag name selectors
- How to modify an HTML element's style
- How to get and update an HTML element's content
- How to modify the DOM
- How to make a GET request with jQuery Ajax
- How to make a POST request with jQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

---

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`
- You must use jQuery version 3.x
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

### Import jQuery

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

## Manual QA Review

It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

## Tasks

### Task 0: No JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):

- You must use `document.querySelector` to select the HTML tag
- You can't use the jQuery API
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```

[Repo: Task 0](#)

### Task 1: With JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```

[Repo: Task 1](#)

### Task 2: Click and Turn Red

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header:

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```

[Repo: Task 2](#)

### Task 3: Add `.red` Class

Write a JavaScript script that adds the class `red` to the

 `<header>` element when the user clicks on the tag DIV#red_header:

- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```

[Repo: Task 3](#)

### Task 4: Toggle Classes

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:

- The `<header>` element must always have one class: red or green, never both at the same time and never empty.
- If the current class is red, when the user clicks on DIV#toggle_header, the class must be updated to green, and vice versa.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```

[Repo: Task 4](#)

### Task 5: List of Elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item:

- The new element must be: `<li>Item</li>`
- The new element must be added to UL.my_list
- You can't use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```

[Repo: Task 5](#)

### Task 6: Change the Text

Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on DIV#update_header:

- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```

[Repo: Task 6](#)

### Task 7: Star Wars Character

Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

- The name must be displayed in the HTML tag DIV#character.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```

[Repo: Task 7](#)

### Task 8: Star Wars Movies

Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

- All movie titles must be listed in the HTML tag UL#list_movies.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
```

[Repo: Task 8](#)

### Task 9: Say Hello!

Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of "hello" from that fetch in the HTML tag DIV#hello.

- The translation of "hello" must be displayed in the HTML tag DIV#hello.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Your script must work when it is imported from the `<head>` tag.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

[Repo: Task 9](#)

### Task 10: No jQuery - Document Loaded

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000):

- You must use `document.querySelector` to select the HTML tag.
- You can't use the jQuery API.
- Note: Your script must be imported from the `<head>` tag, not at the end of the HTML.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

[Repo: Task 10](#)

### Task 11: List, Add, Remove

Write a JavaScript script that adds, removes, and clears LI elements from a list when the user clicks:

- The new element must be: `<li>Item</li>`
- The new element must be added to UL.my_list
- When the user clicks on DIV#add_item, a new element is added to the list.
- When the user clicks on DIV#remove_item, the last element is removed from the list.
- When the user clicks on DIV#clear_list, all elements of the list are removed.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Your script must work when imported from the `<head>` tag.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

[Repo: Task 11](#)

### Task 12: Say Hello to Everybody!

Write a JavaScript script that fetches and prints how to say "Hello" depending on the language:

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en, etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate.
- The translation of "Hello" must be displayed in the HTML tag DIV#hello.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Your script must work when imported from the `<head>` tag.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

[Repo: Task 12](#)

### Task 13: And Press ENTER

Write a JavaScript script that fetches and prints how to say "Hello" depending on the language:

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en, etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code.
- The translation of "Hello" must be displayed in the HTML tag DIV#hello.
- You can't use `document.querySelector` to select the HTML tag.
- You must use the jQuery API.
- Your script must work when imported from the `<head>` tag.
- Please test with this HTML file in your browser:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```

[Repo: Task 13](#)

---
## Author

[GitHub - Alexander Udeogaranya](https://github.com/Dr-dyrane)
