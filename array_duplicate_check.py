import csv

def load_csv_to_array(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def remove_duplicates(data):
    seen = set()
    duplicates = 0
    total_rows = len(data)
    
    new_data = []
    
    for row in data:
        row_tuple = tuple(row)  
        if row_tuple not in seen:
            seen.add(row_tuple)
            new_data.append(row)
        else:
            duplicates += 1
    
    return total_rows, duplicates, len(new_data), new_data

# Arrau
file_path = 'all_data.csv'
data_array = load_csv_to_array(file_path)

total_rows, total_duplicates, rows_now, clean_data = remove_duplicates(data_array)

print(f"Total rows before: {total_rows}")
print(f"Total duplicates found: {total_duplicates}")
print(f"Total rows now: {rows_now}")
