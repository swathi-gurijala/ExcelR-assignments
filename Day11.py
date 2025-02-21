#day11

import requests
from bs4 import BeautifulSoup

def fetch_webpage_title(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Raise an exception if the request was not successful
        response.raise_for_status()

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and return the title of the webpage
        title = soup.title.string if soup.title else 'No title found'
        return title

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Test the function with the given URL
test_url = 'https://example.com'
title = fetch_webpage_title(test_url)
print("Webpage URL:", test_url)
print("Webpage Title:", title)
