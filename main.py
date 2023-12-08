import subprocess
import os

# Get the current directory of the main script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Specify the paths to your scripts
webscrape = os.path.join(current_directory, 'bfro/webscrapers/complete_webscrape.py')
update_ws = os.path.join(current_directory, 'bro/webscrapers/update_webscrape.py')
clean = os.path.join(current_directory, 'bfro/cleaning_tools/clean_json.py')
init_database = os.path.join(current_directory, 'bfro/data/initiate_db.py')
update_db = os.path.join(current_directory, 'bfro/data/update_db.py')
remove_local = os.path.join(current_directory, 'bfro/cleaning_tools/remove_local_files.py')

try:
    subprocess.run(['python', webscrape])
    subprocess.run(['python', clean])
    subprocess.run(['python', init_database])
    subprocess.run(['python', remove_local])
    print('Database updated')
except Exception as e:
    print(f'Error occured updating database: {e}')

