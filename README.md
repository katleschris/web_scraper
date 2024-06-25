<h1 align="center">Web Scraper to collect data on secondary schools in Victoria, Australia from Goodschools.com  </h1>

<div align="center" >
  <img src="https://img.shields.io/badge/made%20by-Katlego%20Leshiba-blue?style=for-the-badge&labelColor=20232a" />
  <img src="https://img.shields.io/badge/Python-20232a?style=for-the-badge&logo=python&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/Django-20232a?style=for-the-badge&logo=django&labelColor=162e16" />
  <img src="https://img.shields.io/badge/CSS-20232a?style=for-the-badge&logo=css&labelColor=2e2f35" />
  <img src="https://img.shields.io/badge/Pandas-20232a?style=for-the-badge&logo=pandas&labelColor=2e2f38" />
  <img src="https://img.shields.io/badge/GeoPy-20232a?style=for-the-badge&logo=geopy&labelColor=2e2f38" />
  
</div>

## Project Overview

This project involves designing and implementing a web scraper to collect data for secondary schools in Australia. The script collects the School Name, Location/Suburb, Sector, Address, Postal Code, geolocation and academic results.

## Pre-requisites and Dependencies

Ensure you have the following installed on your machine:

1. **Python 3.x**: You can download Python from the [official website](https://www.python.org/downloads/).

2. **pip**: Python package installer, which comes pre-installed with Python.

3. **Required Python Packages**:
   - `requests`
   - `beautifulsoup4`
   - `pandas`

You can install the necessary packages using the `requirements.txt` file provided.

## Installation

1. **Clone the repository** (or download the script):
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script, execute the following command:
```sh
python3 webScraper.py
```

The script will retrieve school data from the specified pages and save it to a CSV file named `schools.csv`.

## Code Overview

### Functions

1. **fetch_page(url)**: Fetches the content of a given URL.
    - Parameters: `url` (str) - The URL to fetch.
    - Returns: `str` - The HTML content of the page, or `None` if an error occurs.

2. **parse_search_results(html)**: Parses the search results from the HTML to extract school URLs.
    - Parameters: `html` (str) - The HTML content of the search results page.
    - Returns: `list` - A list of school URLs.

3. **fetch_school_info(url)**: Fetches and parses school information from a given school URL.
    - Parameters: `url` (str) - The URL of the school's page.
    - Returns: `dict` - A dictionary containing the school's information, or `None` if an error occurs.

4. **main()**: Main function to scrape school data and save it to a CSV file.
    - Loops through multiple pages of search results, retrieves school URLs, fetches school information, and saves the data to a CSV file.

## Example Output

The output CSV file `schools.csv` will contain columns such as:
- `School Name`
- `Location`
- `Sector`
- `Address`
- `Postal Code`
- `Latitude`
- `Longitute`
- `Scores of 40+`
- `Median Score`
- `Satisfactory completions of VCE`
- `Satisfactory completions of VET`

## Error Handling

The script includes basic error handling for network requests and HTML parsing. If an error occurs while fetching a page or parsing its content, a message will be printed to the console, and the script will continue to the next item.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
