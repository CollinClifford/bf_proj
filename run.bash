#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | awk '/=/ {print $1}')
fi

SCHEMA_NAME=public
TABLE_NAME=reports

# Check if the table exists
if PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "\dt $SCHEMA_NAME.$TABLE_NAME" | grep -q $TABLE_NAME; then
    echo "Updating database table name $SCHEMA_NAME.$TABLE_NAME"
    # Scrapes just the recent sightings.
    python3 ./bfro/webscrapers/update_webscrape.py
    # Step #1 of cleaning tools: removes any unwanted columns that may have been processed by webscraping tool
    python3 ./bfro/cleaning_tools/clean_json.py
    # TODO: cleaning tools that clean year, date, location
    # Updates the database w/ new reports
    python3 ./bfro/data/update_db.py
else
    # Builds a new table for BFRO sightings
    echo "Initializing new database table named $SCHEMA_NAME.$TABLE_NAME"
    # Scrapes the entire reports website by county, city and then report
    python3 ./bfro/webscrapers/complete_webscrape.py
    # Step #1 of cleaning tools: removes any unwanted columns that may have been processed by webscraping tool
    python3 ./bfro/cleaning_tools/clean_json.py
    # TODO: cleaning tools that clean year, date, location
    # Initializes a new table and inserts reports
    python3 ./bfro/data/initiate_db.py
fi
