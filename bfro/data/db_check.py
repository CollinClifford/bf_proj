import psycopg2
import json
from dotenv import load_dotenv
import os
from sql_commands.create_table import *
from sql_commands.insert_data import *

def main():

    # Initializes environmental variables
    count = 0
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

    try:
        # Connects to PostgreSQL db
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        # Executes the SELECT query
        try:
            cursor.execute("SELECT * FROM reports;")
            count = cursor.rowcount
        except:
            count = 0
        # Gets the count of rows
        

        # Commits and closes connection
        conn.commit()
        conn.close()
        
        print(count)
        return count

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
