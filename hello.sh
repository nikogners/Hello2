#!/bin/bash
# Hello2 - A simple Hello World application in Bash

# Function to generate greeting
greet() {
    local name=${1:-"World"}
    echo "Hello, $name!"
}

# Main execution
echo "Running Hello2 application..."
greet
greet "Bash"
greet "User"