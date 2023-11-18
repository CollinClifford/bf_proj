import psycopg2
import json
from dotenv import load_dotenv
import os
from sql_commands.create_table import *
from sql_commands.insert_data import *

def main():

    # Initializes environmental variables
    load_dotenv()
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    ssl_mode = os.environ.get("SSL_MODE")

    db_params = {
        'host': db_host,
        'database': db_name,
        'user': db_user,
        'password': db_password,
        'port': db_port,
        'sslmode': ssl_mode
    }

    # Finds absolute path of json file
    json_file_path = './bfro/data/clean_data/cleaned_columns_bfro_data.json'
    json_file_path = os.path.abspath(json_file_path)

    # Tries to open file, if not throws error
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Conneects to PostgreSQL db
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Drops table for clean up but it shouldn't exist
        cursor.execute("DROP TABLE IF EXISTS reports;")

        # Creates table
        create_table(cursor)
        
        # Inserts each record
        for record in json_data:
            insert_data(cursor, record)

        # Commits and closes connection
        conn.commit()
        conn.close()

        print("Script executed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
