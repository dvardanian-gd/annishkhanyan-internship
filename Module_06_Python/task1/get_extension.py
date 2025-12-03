"""
Simple script to check and print the extension of a filename.
"""

#!/usr/bin/env python3
import re
import sys

def extension_check(filename):
    """Checks whether the given filename contains an extension."""
    
    match = re.match(r'.*?\.([^.]+)$', filename)

    if not match:
        raise ValueError("No file extension found")

    print(f"File extension is {match.group(1)}")



def main():
    """Main function that handles argument parsing and calls extension_check."""
    if len(sys.argv) != 2:
        print("Usage: python3 get_extension.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        extension_check(filename)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
