import subprocess
import os

# Get the current directory of the main script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the paths to your scripts
webscrape = os.path.join(current_directory, 'webscrapers/complete_webscrape.py')
update_ws = os.path.join(current_directory, 'webscrapers/update_webscrape.py')
clean = os.path.join(current_directory, 'webscrapers/functions/clean_json.py')
init_database = os.path.join(current_directory, 'bigfoot_factory/initiate_db.py')
update_db = os.path.join(current_directory, 'bigfoot_factory/update_db.py')
# remove_local = os.path.join(current_directory, 'bfro/cleaning_tools/remove_local_files.py')
clean_db = os.path.join(current_directory, 'bigfoot_factory/clean_db.py')
count_rows = os.path.join(current_directory, 'bigfoot_factory/db_check.py')

# Capture the output of db_check.py
count_result = subprocess.run(['python', count_rows], capture_output=True, text=True)

try:
    count_str = count_result.stdout.strip()

    # Print the raw output for debugging
    print("Raw output from db_check.py:", count_result.stdout)

    # Check if the output is a non-empty string before converting to int
    if count_str and count_str.isdigit():
        count = int(count_str)
        
        if count <= 0:
            subprocess.run(['python', webscrape])
            subprocess.run(['python', clean])
            subprocess.run(['python', init_database])
            subprocess.run(['python', clean_db])
            print('Database updated')
        else:
            subprocess.run(['python', update_ws])
            subprocess.run(['python', clean])
            subprocess.run(['python', init_database]) # subprocess.run(['python', update_db])
            subprocess.run(['python', clean_db])
            print("Database updated")
    else:
        print("count_str failed:", count_str)

except Exception as e:
    print(f'main.py failed: {e}')
