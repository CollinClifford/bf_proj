import psycopg2
from dotenv import load_dotenv
import os
from stored_proc_python import *

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

    proc_array = [
        add_day_of_week_column,
        set_day_of_week_column,
        clean_day_column,
        change_date_to_day,
        add_date_column,
        format_date,
        update_follow_up_one,
        update_follow_up_two,
        add_month_number_column,
        set_month_number_column,
        update_seasons_column,
        remove_submitted,
        remove_by,
        remove_witness,
        add_submitted_by_date,
        remove_on,
        remove_comma,
        set_date,
        set_month,
        formate_date,
        clean_year,
        trim_year
    ]

    try:
        # Conneects to PostgreSQL db
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        for proc in proc_array:
            cursor.execute(proc)

        conn.commit()
        conn.close()
    except Exception as e:
        print(f'Failed to update database: {e}')

if __name__ == "__main__":
    main()
