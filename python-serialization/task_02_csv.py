#!/usr/bin/env python3

"""Module for converting CSV files to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to a JSON file."""
    try:
        with open(filename, "r") as csv_f:
            reader = csv.DictReader(csv_f)
            data = list(reader)
        with open("data.json", "w") as js_f:
            json.dump(data, js_f)
        return True
    except Exception:
        return False
