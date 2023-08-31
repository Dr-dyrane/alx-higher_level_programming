#!/bin/bash
# This script sends a POST request to a URL with specified parameters and displays the response body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
