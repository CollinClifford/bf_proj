import os

def delete_json_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

# Example usage
if __name__ == "__main__":
    # Specify the path to the JSON file you want to delete
    # Get the current directory of the main script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    raw = os.path.join(current_directory, 'bfro/data/raw_data/bfro_data.json')
    clean = os.path.join(current_directory, 'bfro/data/clean_data/cleaned_columns_bfro_data.json')

    # Call the function to delete the JSON file
    delete_json_file(raw)
    delete_json_file(clean)
