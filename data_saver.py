import json
def save_data(file_name,items):
    with open(f'{file_name}.json', 'w') as file:
        json.dump(items, file, indent=4)
    print(f"Data saved to {file_name}.json")