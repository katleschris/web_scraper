import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def fetch_page(url):
    """
    Fetch the content of a given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to retrieve URL {url}: {e}")
        return None
    

def parse_search_results(html):
    """
    Parse the search results from the HTML to extract school URLs.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        search_results_div = soup.find("div", {"id": "search-results"})
        media_body_divs = search_results_div.find_all("div", {"class": "media-body"})
        return [a_tag.find("a", href=True)["href"].strip() for a_tag in media_body_divs if a_tag.find("a", href=True)]
    except AttributeError as e:
        print(f"Error parsing search results HTML: {e}")
        return []
