import sys
import webbrowser
"""This code is website automator.py but with all the error checks """

URLS = {
#enter your own urls here these are just examples
    "personal": [
        "https://www.youtube.com",
        "https://www.twitch.tv",
        "https://9animetv.to/home",
        "https://www.netflix.com/browse"
    ],
    "work": []
}

def open_webpages(urls):
    """Opens each URL in the provided list with error handling."""
    if not urls:
        print("No URLs to open in this set.")
        return

    for url in urls:
        try:
            print(f"Opening: {url}")
            webbrowser.open(url)
        except Exception as e:
            print(f"Failed to open {url}: {e}")

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("No set name provided. Please provide 'personal' or 'work'.")

        set_name = sys.argv[1]
        
        if set_name not in URLS:
            raise KeyError(f"'{set_name}' is not a valid set name. Choose from: {', '.join(URLS.keys())}")

        urls = URLS[set_name]
        open_webpages(urls)

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
