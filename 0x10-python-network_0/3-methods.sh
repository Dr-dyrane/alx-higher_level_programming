#!/bin/bash
# This script displays all HTTP methods the server will accept for the specified URL
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
