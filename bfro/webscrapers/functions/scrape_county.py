from bs4 import BeautifulSoup
import requests
from functions.scrape_city import scrape_city

def scrape_county(state_url):
    # sets variables inmport for the condition
    base_url = "https://www.bfro.net"
    phrase = f"show_county_reports.asp?state={state_url[-2:]}&county="
    city_links = []
    city_data = {}

    # Scrapes, then parses the counties
    response_county = requests.get(state_url)
    soup_county = BeautifulSoup(response_county.text, 'html.parser')

    # Looks for href in the county's site and then checks to see if it matches the phrase variable
    all_links = soup_county.find_all('a', href=True)
    for link in all_links:
        if link["href"].startswith(phrase):
            city_links.append(f'{base_url}/GDB/{link["href"]}')

    # runs the scrape_city function for each city link in the list
    for city_link in city_links:
        city_data = scrape_city(city_link)

    return city_data