"""
This module is for the import of the data in a JSON-file
"""

import json

# Path to JSON-File
FILE_PATH = "./DataSet/city.json"

# Read JSON-File
with open(FILE_PATH, encoding="utf-8") as file:
    data = json.load(file)


def export_data():
    """
    This function exports the JSON date.

    Returns:
        JSON: The data from the JSON file.
    """
    return data
