import pandas as pd
import os

# Define the paths
csv_file = 'bounding_boxes_02.csv'  # Update this path
images_folder = 'bounding box'
labels_folder = 'label'

# Create labels directory if it doesn't exist
os.makedirs(labels_folder, exist_ok=True)

# Read the CSV file
df = pd.read_csv(csv_file)

# Get image dimensions (you may want to automate this based on your images)
image_dimensions = {}  # Dictionary to store image dimensions

for index, row in df.iterrows():
    image_name = row['name']
    xmax = row['xmax']
    ymax = row['ymax']
    xmin = row['xmin']
    ymin = row['ymin']
    
    # Get image size
    if image_name not in image_dimensions:
        from PIL import Image
        
        img_path = os.path.join(images_folder, image_name)
        with Image.open(img_path) as img:
            width, height = img.size
            image_dimensions[image_name] = (width, height)

    width, height = image_dimensions[image_name]
    
    # Normalize coordinates
    x_center = (xmin + xmax) / 2 / width
    y_center = (ymin + ymax) / 2 / height
    norm_width = (xmax - xmin) / width
    norm_height = (ymax - ymin) / height

    # Write to the corresponding text file
    label_file_path = os.path.join(labels_folder, image_name.replace('.jpg', '.txt'))  # Adjust extension as needed
    with open(label_file_path, 'a') as label_file:
        # Assuming single class for simplicity; replace <class_id> with actual class ID if needed
        class_id = 0  # Change this according to your class mapping
        label_file.write(f"{class_id} {x_center} {y_center} {norm_width} {norm_height}\n")

print("Conversion completed!")