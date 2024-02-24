import json
import os

def append_to_json(data):

    existing_data = []

    # Absolute path for JSON
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
    json_file_path = os.path.join(project_directory, 'datalake\\bfro_data.json')
    
    # Checks if JSON exists
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print(f'Error loading existing data: {e}.')

    # Stores JSON data
    existing_data.append(data)
    
    existing_report_numbers = [item.get('report_number') for item in existing_data]

    # Appends all reports from webscraper.
    if data:
        if data['report_number'] not in existing_report_numbers:
            try:
                with open(json_file_path, 'w', encoding='utf-8') as file:
                    json.dump(existing_data, file, indent=2)
            except Exception as e:
                print(f'{data['report_number']} failed: {e}.')
    else:
        print('Nothing to append.')

    