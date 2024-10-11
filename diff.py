#!/usr/bin/env python3

import sys
import json

def is_valid_prefix(prefix, full_list, min_terms=10):
    if len(prefix) < min_terms:
        return False
    return prefix == full_list[:len(prefix)]

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    # Read the JSON list from stdin
    try:
        prefix_list = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        print("Error: Invalid JSON input from stdin")
        sys.exit(1)

    # Read the JSON file
    try:
        with open(sys.argv[1], 'r') as f:
            full_list = json.load(f)
    except (IOError, json.JSONDecodeError):
        print(f"Error: Unable to read or parse JSON file {sys.argv[1]}")
        sys.exit(1)

    # Check if the lists are valid
    if not isinstance(prefix_list, list) or not isinstance(full_list, list):
        print("Error: Both inputs must be JSON lists")
        sys.exit(1)

    # Check if one is a valid prefix of the other
    if is_valid_prefix(prefix_list, full_list) or is_valid_prefix(full_list, prefix_list):
        print("PASS")
        sys.exit(0)
    else:
        print("FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
