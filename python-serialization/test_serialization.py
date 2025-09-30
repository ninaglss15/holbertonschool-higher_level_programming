#!/usr/bin/python3
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {"name": "John Doe", "age": 30, "city": "New York"}

# Sérialisation et sauvegarde
serialize_and_save_to_file(data, "data.json")
print("Data saved!")

# Lecture et désérialisation
new_data = load_and_deserialize("data.json")
print("Deserialized data:")
print(new_data)
