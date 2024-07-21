import pandas as pd
import csv

# File paths
input_file_path = 'D:/360DT/Course_Scanner/new_new/course2.csv'
output_file_path = 'D:/360DT/Course_Scanner/new_new/course_cleaned.csv'

# Read and clean the CSV file
with open(input_file_path, 'r', newline='', encoding='utf-8') as infile, open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)  # Read the header
    writer.writerow(header)  # Write the header to the output file
    
    for row in reader:
        if len(row) == len(header):
            # Remove everything after '\n' and remove '\n' itself from the 'coursename' column
            row[1] = row[1].split('\n')[0]
            writer.writerow(row)

# Load the cleaned CSV file into a pandas DataFrame
df = pd.read_csv(output_file_path)

print("Processed CSV file loaded successfully.")
