import json

def read_json_to_list(file_path:str):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):  # Ensure the data is a list
                return data
            else:
                raise ValueError("JSON structure is not a list")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return []
    except ValueError as e:
        print(e)
        return []


