from bs4 import BeautifulSoup
from functions.scrape_all import scrape_all

# Starts the webscraper
if __name__ == "__main__":
    try:
        print('1. Complete webscrape')
        scrape_all()
    except Exception as e: 
        print(f"Error in main script: {e}")