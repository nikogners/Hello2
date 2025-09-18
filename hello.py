#!/usr/bin/env python3
"""
Hello2 - A simple Hello World application
"""

def greet(name="World"):
    """
    Generate a greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def main():
    """Main function to run the Hello2 application."""
    print(greet())
    print(greet("Python"))
    print(greet("User"))

if __name__ == "__main__":
    main()