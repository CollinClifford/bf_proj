from bs4 import BeautifulSoup
from functions.scrape_recent_sightings import scrape_recent_sightings

# Starts the webscraper
if __name__ == "__main__":
    try:
        scrape_recent_sightings()
    except Exception as e:
        print(f"Error in main script: {e}")