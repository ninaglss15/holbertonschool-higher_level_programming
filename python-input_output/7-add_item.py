#!/usr/bin/python3
"""
Convert a Python list to a JSON string and print it.
"""

import json

my_list = ["Best", "School"]
json_string = json.dumps(my_list)
print(json_string)
