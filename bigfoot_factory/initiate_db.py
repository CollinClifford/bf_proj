import psycopg2
import json
import csv
from dotenv import load_dotenv
import os
from sql_commands.create_table import *
from sql_commands.insert_data import *

def main():

    # Initializes environmental variables
    load_dotenv()
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')
    ssl_mode = os.environ.get('SSL_MODE')

    db_params = {
        'host': db_host,
        'database': db_name,
        'user': db_user,
        'password': db_password,
        'port': db_port,
        'sslmode': ssl_mode
    }

    # Absolute path for JSON
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..'))
    json_file_path = os.path.join(project_directory, 'datalake\\cleaned_columns_bfro_data.json')
    csv_file_path = os.path.join(project_directory, 'datalake\\county_locations.csv')

    # Tries to open file, if not throws error
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
        
        # Conneects to PostgreSQL db
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Drops table for clean up but it shouldn't exist
        try: 
            cursor.execute('DROP TABLE IF EXISTS reports;')
            cursor.execute('DROP TABLE IF EXISTS lat_long;')
        except Exception as e:
            print(f'Drop table failed: {e}.')
        # Creates table
        try:
            create_table(cursor)
            create_location_table(cursor)
        except:
            print(f'create_table failed.')
        # Inserts each record
        for record in json_data:
            try:
                insert_data(cursor, record)
            except Exception as e:
                print(f'{record} not inserted.')
        with open(csv_file_path) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            
            # Skip the headers
            next(csv_data)
            
            for row in csv_data:
                try:
                    
                    insert_location_data(cursor, row)
                except Exception as e:
                    print(f'{row} not inserted.')
        # Commits and closes connection
        conn.commit()
        conn.close()

    except Exception as e:
        print(f'initiate_db failed: {e}')

if __name__ == '__main__':
    print('3. Initiate DB')
    main()
