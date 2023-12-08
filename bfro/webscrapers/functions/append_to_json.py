import json
import os



def append_to_json(data):
    
    # Initializes variables
    existing_data = []

    # Finds the absolute path for the JSON
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
    json_file_path = os.path.join(project_directory, 'data\\raw_data\\bfro_data.json')
    
    # Checks if json exists
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        print(f"Error loading existing data: {e}")

    # Stores json data
    existing_data.append(data)
    # Checks if report number is in JSON data and appends if not
    if data:
        with open(json_file_path, 'w', encoding='utf-8') as file:
            print(f"Appended data to report number: {data['report_number']} to {json_file_path.split('/')[-1]}")
            json.dump(existing_data, file, indent=2)
    else:
        print("nothing to append")
