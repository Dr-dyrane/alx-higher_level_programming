#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response in silent mode (-s)
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
