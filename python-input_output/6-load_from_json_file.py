#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file (UTF-8) and return it."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
