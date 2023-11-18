# Bigfoot Tracking and Analysis Project - Version 1.1 (In Progress)

## Overview

The Bigfoot Tracking and Analysis Project is an automated system designed to collect and analyze sightings of Bigfoot from the Bigfoot Field Researchers Organization (BFRO) website. The project runs daily at 12:00 UTC, utilizing web scraping to gather data on Bigfoot sightings across various US counties.

## Components

### File Structure

- `bf_tracking/bfro/cleaning_tools/clean_json.py`
- `bf_tracking/bfro/data/sql_commands/create_table.py`
- `bf_tracking/bfro/data/sql_commands/insert_data.py`
- `bf_tracking/bfro/data/sql_commands/select_all.py`
- `bf_tracking/bfro/data/bfro_data.json`
- `bf_tracking/bfro/data/initiate_db.py`
- `bf_tracking/bfro/data/update_db.py`
- `bf_tracking/bfro/webscrapers/functions/append_to_json.py`
- `bf_tracking/bfro/webscrapers/functions/scrape_bfro.py`
- `bf_tracking/bfro/webscrapers/functions/scrape_city.py`
- `bf_tracking/bfro/webscrapers/functions/scrape_site.py`
- `bf_tracking/bfro/webscrapers/functions/scrape_state.py`
- `bf_tracking/bfro/webscrapers/complete_webscrape.py`
- `bf_tracking/bfro/webscrapers/update_webscrape.py`
- `bf_tracking/WIP` (Work in Progress, unused items)
- `bf_tracking/readme.md`
- `bf_tracking/run.bash`
- `bf_tracking/.gitignore`
- `bf_tracking/requirements.txt`

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

## Release Plan

- **Version 1.2:**
    - Clean Year and Date columns.

- **Version 1.3:**
    - Clean submitted_by column.

- **Version 1.4:**
    - Clean state, county, nearest_town columns.

## Installation and Execution

1. **Clone Repository:**
    ```bash
    git clone [repository_url]
    cd bf_tracking
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
3. ***Configure Environment Variables:***
    - Create a `.env` file in the project root with the necessary environment variables.
4. ***Run the Program:***
    - Execute the bash script:
    ```bash
    ./run.bash
    - Alternatively, execute individual Python scripts based on your requirements.

This setup ensures a seamless installation and execution of the Bigfoot Tracking and Analysis Project.