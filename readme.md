# Bigfoot Tracking and Analysis Project - Version 1.1

## Overview

The Bigfoot Tracking and Analysis Project is an automated system designed to collect and analyze sightings of Bigfoot from the Bigfoot Field Researchers Organization (BFRO) website.

## Version 1.1

- Determines whether the entire website should be scraped or only the recent sightings
- Runs webscraping tools
- Cleans columns of unwanted keys from the webscraping process
- Inserts json data into PostgreSQL databse

## Components

### File Structure

- `bf_proj/bfro/cleaning_tools/clean_json.py`
- `bf_proj/bfro/data/clean_data/cleaned_columns_bfro_data.json`
- `bf_proj/bfro/data/raw_data/bfro_data.json`
- `bf_proj/bfro/data/sql_commands/create_table.py`
- `bf_proj/bfro/data/sql_commands/insert_data.py`
- `bf_proj/bfro/data/sql_commands/select_all.py`
- `bf_proj/bfro/data/initiate_db.py`
- `bf_proj/bfro/data/update_db.py`
- `bf_proj/bfro/webscrapers/functions/append_to_json.py`
- `bf_proj/bfro/webscrapers/functions/scrape_all.py`
- `bf_proj/bfro/webscrapers/functions/scrape_city.py`
- `bf_proj/bfro/webscrapers/functions/scrape_county.py`
- `bf_proj/bfro/webscrapers/functions/scrape_new_report.py`
- `bf_proj/bfro/webscrapers/functions/scrape_recent_sighting.py`
- `bf_proj/bfro/webscrapers/functions/scrape_report.py`
- `bf_proj/bfro/webscrapers/complete_webscrape.py`
- `bf_proj/bfro/webscrapers/update_webscrape.py`
- `bf_proj/.gitignore`
- `bf_proj/readme.md`
- `bf_proj/requirements.txt`
- `bf_proj/run.bash`

### Packages Used

- `json`
- `os`
- `requests`
- `beautifulsoup`
- `psycopg2`
- `dotenv`

## Workflow

1. **Database Check:**
    - The project checks if the database exists in the ElephantSQL instance.

2. **Web Scraping:**
    - If the database doesn't exist, `complete_webscrape.py` is executed, scraping the entire BFRO website and returning information on Bigfoot sightings in every US county.
    - If the database exists, `update_webscrape.py` is executed. This script browses recent reports, checks for the report_number in the database, and appends new reports.
3. **Clean Data:**
    - Cleans unwanted columns
4. **Updates Database:**
    - Checks to see if reports exist in database, inserts if not.

## Release Plan

- **Version 1.2:**
    - Clean Year and Date columns.

- **Version 1.3:**
    - Clean submitted_by column.

- **Version 1.4:**
    - Clean state, county, nearest_town columns.

## Installation and Execution

*Note:* This project uses python3.

1. **Clone Repository:**
    ```bash
    git clone [repository_url]
    cd bf_proj
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
3. ***Configure Environment Variables:***
    - Create a `.env` file in the project root with the necessary environment variables.
4. ***Run the Program:***
    - Execute the bash script:
    ```bash
    bash run.bash
    - Alternatively, execute individual Python scripts based on your requirements.

This setup ensures a seamless installation and execution of the Bigfoot Tracking and Analysis Project.