import pandas as pd
import os

# Define the path to the CSV file and the output directory
csv_file_path = 'updated_annotations_yolo_01_with_numbers.csv'
output_dir = 'labeldata'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Traverse through each row in the DataFrame
for index, row in df.iterrows():
    # Extract the necessary information
    file_name = row['name']  # Adjust this column name as needed
    category = row['category_number']  # Adjust this column name as needed
    x_center = row['x_center']  # Adjust this column name as needed
    y_center = row['y_center']  # Adjust this column name as needed
    width = row['width']  # Adjust this column name as needed
    height = row['height']  # Adjust this column name as needed

    # Create the output file name
    txt_file_name = f"{os.path.splitext(file_name)[0]}.txt"
    txt_file_path = os.path.join(output_dir, txt_file_name)

    # Prepare the output format
    output_line = f"{category} {x_center} {y_center} {width} {height}\n"

    # Write to the text file
    with open(txt_file_path, 'a') as f:
        f.write(output_line)
