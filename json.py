import json

bio_data = {
    "name": "Amanulah",
    "age": 23,
    "job": "developer"
}

file_path = r"C:\Users\User\Desktop\output.json"  # Removed extra space

with open(file_path, 'w') as file:
    json.dump(bio_data, file, indent=4)
    print(f"json file '{file_path}' was created")

