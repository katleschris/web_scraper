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
