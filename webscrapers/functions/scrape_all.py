from bs4 import BeautifulSoup
import requests
from functions.scrape_county import scrape_county

def scrape_all():

    # Initializes variables
    base_url = 'https://www.bfro.net'
    states_url = f'{base_url}/GDB/default.asp'
    phrase = '/GDB/state_listing.asp?state='
    county_data = {}
    county_links = []

    # Parses county website
    response_county = requests.get(states_url)
    soup_county = BeautifulSoup(response_county.text, 'html.parser')

    # Checks each link for phrase and appends it to list
    all_links = soup_county.find_all('a', href=True)
    for link in all_links:
        if link["href"].startswith(phrase):
            county_links.append(f'{base_url}{link["href"]}')

    # Call scrape_county for each link
    for state_link in county_links:
        try:
            county_data = scrape_county(state_link)
        except Exception as e:
            print(f'{state_link} failed to pass.')

    return county_data