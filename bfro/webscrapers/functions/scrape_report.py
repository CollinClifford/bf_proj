from bs4 import BeautifulSoup
import requests
from functions.append_to_json import append_to_json

def scrape_report(site_url):

    # Initializes variables
    report_data = {}
    hold_array = []
    quote_array = []
    
    # Gets the report url and parses it
    response_report = requests.get(site_url)
    soup_report = BeautifulSoup(response_report.text, 'html.parser')

    # Sets up report number and classification for the json file
    report_data["report_number"] = soup_report.find('span', class_='reportheader').text.split(" # ")[1]
    report_data["report_classification"] = soup_report.find('span', class_='reportclassification').text.replace('(', '').replace(')','')

    # Finds the submitted by section aand the brief summary section
    header = soup_report.find_all('span', class_='field')

    # Inserts the submitted by and then holds the summary
    for section in header:
        if 'submitted' in section.text.lower():
            report_data['submitted_by'] = section.text
        else:
            hold_array.append(section.text)
    
    # Inserts summary
    report_data["summary"] = hold_array[0]

    # Finds the bulk of the information on the page
    fields = soup_report.find_all("p")

    # Iterates 13 fields, cleans their keys and inserts their values
    for index, field in enumerate(fields):
        if index == 13:
            break
        field = field.text.split(": ", 1)
        if len(field) >= 2 and field[1]:
            if " " in field[0]:
                report_data[field[0].replace(" ", "_").lower()] = field[1]
            else:
                report_data[field[0].lower()] = field[1]
        else:
            if " " in field[0]:
                report_data[field[0].replace(" ", "_").lower()] = ""
            else:
                report_data[field[0].lower()] = ""

    # Finds if there is a follow-up section and inserts it
    for fi in fields:
        if 'follow-up' in fi.text.lower():
            report_data['follow_up'] = fi.text
    
    # finds if there is follow up details and inserts them
    quotes = soup_report.find_all('blockquote')

    for quote in quotes:
        quote_array.append(quote.text)
        report_data['follow_up_details'] = quote_array[0]
    
    # Calls the append_to_json function
    append_to_json(report_data)
    
    return report_data
