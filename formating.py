import pandas as pd
from PIL import Image
import os

def normalize_coordinates(row, images_folder):
    image_name = row['image_name']
    image_path = os.path.join(images_folder, image_name)

    with Image.open(image_path) as img:
        image_width, image_height = img.size

    row['normalized_ymax'] = row['ymax'] / image_height
    row['normalized_ymin'] = row['ymin'] / image_height
    row['normalized_xmax'] = row['xmax'] / image_width
    row['normalized_xmin'] = row['xmin'] / image_width

    return row

# Path to the CSV file and images folder
csv_file = 'bounding_boxes_02.csv'
images_folder = 'downloaded_images'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Apply normalization to each row
normalized_df = df.apply(lambda row: normalize_coordinates(row, images_folder), axis=1)

# Save the normalized coordinates to a new CSV file
normalized_df.to_csv('normalized_bounding_boxes.csv', index=False)

print("Normalized coordinates saved to 'normalized_bounding_boxes.csv'")
