#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response (for status code 200)
curl -sL "$1"
