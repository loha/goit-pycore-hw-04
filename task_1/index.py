import csv
import os
from pathlib import Path

def total_salary(path: str) -> tuple:
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    total_salary = 0
    rows_count = 0
    try:
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                total_salary += int(row[1])
                rows_count += 1
    except (IOError, csv.Error) as e:
        print(f"Error reading CSV file: {e}")
    
    avarage_salary = int(total_salary/rows_count if rows_count > 0 else 0)

    return total_salary, avarage_salary
    
total_salary, avarage_salary = total_salary(Path(__file__).with_name('data.csv'))

print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {avarage_salary}")