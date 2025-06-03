#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Dictionnaire à sauvegarder
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Sauvegarde dans un fichier
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# Lecture depuis le fichier
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
