import csv
import os
from pprint import pprint
from pathlib import Path

def get_cats_info(path: str) -> list:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    data = []
    try:
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append({
                    "id": row[0],
                    "name": row[1],
                    "age": row[2],
                })
    except (IOError, csv.Error) as e:
        print(f"Error reading CSV file: {e}")
    
    return data

cats_info = get_cats_info(Path(__file__).with_name('data.csv'))

pprint(cats_info)