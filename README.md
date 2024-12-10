# How to use the script

## Features
### Predefined URL Sets:

-personal: Contains links to personal websites like YouTube, Twitch, etc.

-work: A placeholder for work-related links (can be customized).
### Error Handling:

-Checks for missing or invalid set names.

-Handles errors if URLs fail to open.

## Requirements
-Python: Version 3.6 or higher.

-Web Browser: The script uses your system's default web browser to open URLs.

## Usage
### 1.Clone the Repository:
git clone "repository-url"

cd "repository-directory"

### 2.Run the Script:
Provide a set name (personal or work) as a command-line argument:

-python script.py personal

This will open all the URLs listed under the personal category.
### 3.Example Commands:

Open personal URLs:

-python script.py personal

Open work URLs:

-python script.py work

## Error Messages
No Set Name Provided:

-Error: No set name provided. Please provide 'personal' or 'work'.

Invalid Set Name Provided:

-Error: 'invalid_set' is not a valid set name. Choose from: personal, work

No URLs in the Selected Set:

-No URLs to open in this set.

Failed to Open URL:

-Failed to open https://example.com: error message

## Customization
You can modify the URLS dictionary in the script to include more categories or URLs:

python
URLS = {

    "personal": [
        "https://www.youtube.com",
        "https://www.twitch.tv"
    ],
    "work": [
        "https://mail.google.com",
        "https://www.github.com"
    ]
}