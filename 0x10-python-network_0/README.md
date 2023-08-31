# Python - Network #0

This project is part of the ALX Higher-Level Programming curriculum and focuses on understanding the basics of network programming in Python. The tasks in this project involve using the `curl` command in Bash and writing Python scripts to interact with web servers and APIs.

## Table of Contents

- [General Info](#general-info)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Usage](#usage)
- [Author](#author)

## General Info

In this project, you will learn about various aspects of web communication, including HTTP, URLs, HTTP methods, headers, and more. You will also practice using the `curl` command in Bash and writing Python scripts to perform various network-related tasks.

## Requirements

- Allowed editors: vi, vim, emacs
- A README.md file is mandatory.
- All Bash scripts should be exactly 3 lines long.
- All Python files should start with `#!/usr/bin/python3`.
- Code should follow PEP 8 style guidelines (`pycodestyle`).
- All modules, classes, and functions should be documented.
- No plagiarism is allowed.

## Tasks

### 0. cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.

The size must be displayed in bytes, and you must use `curl`.

### 1. cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response for a 200 status code response.

You must use `curl`.

### 2. cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

You must use `curl`.

### 3. cURL only methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You must use `curl`.

### 4. cURL headers

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.

A header variable `X-School-User-Id` must be sent with the value `98`.

You must use `curl`.

### 5. cURL POST parameters

Write a Bash script that takes in a URL, sends a POST request to the URL, and displays the body of the response.

Two variables, `email` and `subject`, must be sent with specific values.

You must use `curl`.

### 6. Find a peak (Python)

Write a Python function that finds a peak in a list of unsorted integers. The function should have the lowest complexity possible.

### 7. Only status code (Bash)

Write a Bash script that sends a request to a URL and displays only the status code of the response. No additional output is allowed, and you cannot use pipes or redirection.

You must use `curl`.

### 8. cURL a JSON file (Bash)

Write a Bash script that sends a JSON POST request to a URL and displays the body of the response.

The script should send the contents of a JSON file in the request body.

You must use `curl`.

### 9. Catch me if you can! (Bash)

Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` and causes the server to respond with a message containing "You got me!" in the body of the response.

You must use `curl`, and you are not allowed to use `echo`, `cat`, or similar commands to display the final result.

## Usage

To execute the Bash scripts, use the following format:
```bash
./script_name.sh URL
```

To execute the Python scripts, use the following format:
```bash
python3 script_name.py
```

## Author

- [Alexander Udeogaranya](https://github.com/Dr-dyrane/alx-higher_level_programming/0x10-python-network_0r)