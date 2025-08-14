import os
from PIL import Image  

# Folder containing original images
input_folder = "images"  

# Folder to save resized images 
output_folder = "resized_images"  

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Desired size (width, height) in pixels
new_size = (1000,500)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        # Open image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        img_resized = img.resize(new_size)

        # Save resized image in output folder
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

        print(f"Resized and saved: {save_path}")

print("All images resized successfully!")