from bs4 import BeautifulSoup
import requests
from bfro.webscrapers.functions.scrape_report import scrape_report

def scrape_city(city_url):

    # Initializes variables
    base_url = "https://www.bfro.net"
    phrase = f"show_report.asp?id="
    report_links = []
    report_data = {}

    # Parses city url
    response_city = requests.get(city_url)
    soup_city = BeautifulSoup(response_city.text, 'html.parser')

    # Looks for all links
    all_links = soup_city.find_all('a', href=True)

    # Checks to see if link has phrase and inserts it into report_links list
    for link in all_links:
        if link["href"].startswith(phrase):
            report_links.append(f'{base_url}/GDB/{link["href"]}')

    # Calls scrape_report function for each report link
    for report_link in report_links:
        report_data = scrape_report(report_link)

    return report_data