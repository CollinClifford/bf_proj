import json
import os

# Checks if Key is allowed and keeps it, otherwise removes the key/value pair
def clean_json(json_data, allowed_keys):
    cleaned_data = []
    for item in json_data:
        cleaned_item = {}
        for key, value in item.items():
            formatted_key = str(key)
            lower_formatted_key = formatted_key.lower()
            if lower_formatted_key in map(str.lower, allowed_keys):
                cleaned_item[formatted_key] = value
            # else:
            #     print(f"Ignored key: {key}")
        cleaned_data.append(cleaned_item)
    return cleaned_data

# Finds the absolute path of the file
current_script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
json_file_path = os.path.join(project_directory, 'bfro/data/raw_data/bfro_data.json')
json_file_path = os.path.abspath(json_file_path)

# Loads json file
with open(json_file_path, 'r') as file:
    original_json = json.load(file)

# Declares allowed keys
allowed_keys = [
    "report_number",
    "report_classification",
    "submitted_by",
    "summary",
    "year",
    "season",
    "month",
    "date",
    "state",
    "county",
    "location_details",
    "nearest_town",
    "nearest_road",
    "observed",
    "also_noticed",
    "other_witnesses",
    "other_stories",
    "time_and_conditions",
    "environment",
    "follow_up",
    "follow_up_details"
]

# Executes clean json
cleaned_json = clean_json(original_json, allowed_keys)

# Loads clean json into a new json file
with open('./bfro/data/clean_data/cleaned_columns_bfro_data.json', 'w') as file:
    json.dump(cleaned_json, file, indent=2)

print("Cleaning completed. Cleaned data saved to cleaned_columns_bfro_data.json.")