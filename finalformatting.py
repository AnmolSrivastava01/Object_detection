import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('annotations_yolo_01.csv')

# Function to extract the category from the image name
def extract_category(image_name):
    return image_name.split('_')[1]

# Extract the category and store it in a new column
df['category'] = df['name'].apply(extract_category)

# Insert the 'category' column as the 6th column (index 5)
df.insert(5, 'category', df.pop('category'))

# Load the conversion dictionary from the JSON file
with open('raw.json', 'r') as file:
    data = json.load(file)

conversion_dict = {item['name']: i for i, item in enumerate(data)}

# Map categories to their corresponding numbers
df['category_number'] = df['category'].map(conversion_dict)

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_annotations_yolo_01_with_numbers.csv', index=False)

print("Category number column added successfully!")
