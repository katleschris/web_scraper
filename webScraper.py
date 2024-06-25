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

def fetch_school_info(url):
    """
    Fetch and parse school information from a given school URL.
    """
    html = fetch_page(url)
    if not html:
        return None
    
    school_info = {}
    try:
        soup = BeautifulSoup(html, 'html.parser')
        school_info["School Name"] = soup.find("h1").text.strip()
        school_info["Location"] = soup.find("h4").text.strip()
        address = soup.find("span", {"class": "map-address load-address"}).text.strip()
        school_info["Sector"] = soup.find("p", {"class": "d-inline float-left"}).text.strip()
        school_info["Address"] = address

        # Regular expression pattern to find the postal code
        # \d+ matches one or more digits, and $ ensures it matches at the end of the string
        postal_code_pattern = r'\d+$'
        # Search for the postal code in the address
        match = re.search(postal_code_pattern, address)
        if match:
            postal_code = match.group()
            school_info["Postal Code"] = postal_code
        else:
            print("Postal code not found")

        #fetch academic results
        academic_results_div = soup.find("div", class_="col-md-6 col-sm-6 col-6")
        if academic_results_div:
            academic_results = academic_results_div.find_all("p")
            for tag in academic_results:
                pattern = r":\s*(\S+)"
                match = re.search(pattern, tag.text)
                if match:
                    value = match.group(1)
                    if 'Scores of 40+' in tag.text:
                        school_info["Scores of 40+"] = value
                    if 'Median Score' in tag.text:
                        school_info["Median Score"] = value
                    if 'VCE' in tag.text:
                        school_info["Satisfactory completions of VCE"] = value
                    if "VET" in tag.text:
                        school_info["Satisfactory completions of VET"] = value
    except AttributeError as e:
        print(f"Error parsing school page {url}: {e}")
        return None
    
    return school_info
