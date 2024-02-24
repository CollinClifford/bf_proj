from bs4 import BeautifulSoup
import requests
from functions.scrape_new_report import scrape_site

def scrape_recent_sightings():
    
    # Initializes variables/website
    base_url = 'https://www.bfro.net'
    new_sightings_url = f'{base_url}/GDB/newadd.asp?Show=AB'
    phrase = 'show_report.asp?id='
    report_data = {}
    new_sightings_links = []

    # Parses new sightings website
    response_new_sightings = requests.get(new_sightings_url)
    soup_new_sightings = BeautifulSoup(response_new_sightings.text, 'html.parser')
    
    # Finds all the links for the reports
    all_links = soup_new_sightings.find_all('a', href=True)
    for link in all_links:
        # Checks if link begins with the report phrase and appends it to list
        if link["href"].startswith(phrase):
            new_sightings_links.append(f'{base_url}/GDB/{link["href"]}')

    # Calls scrape_site function for each link in the list
    for new_sighting_link in new_sightings_links:
        try:
            report_data = scrape_site(new_sighting_link)
        except Exception as e:
            print(f'{new_sighting_link} failed to pass.')

    return report_data
