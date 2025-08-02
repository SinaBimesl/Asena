import json

def handle_error(error):
    """
    Just For error Handling
    """
    if isinstance(error, PermissionError):
        print("Error: You need root privileges to do this action.")
    elif isinstance(error, FileNotFoundError):
        print("Error: The file does not exist.")
    elif isinstance(error, json.JSONDecodeError):
        print("Error: The JSON file is corrupted.")
    elif isinstance(error, ValueError):
        print("Error: Invalid Value.")
    else:
        print(f"Unexpected error: {error}")
  