import cv2
import os

# Source and output directories
source_dir = 'input/image' #give your input file path
output_dir = 'output/images' #give your output file path

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all files in the source directory
image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

for image_file in image_files:
    # Build the full paths
    image_path = os.path.join(source_dir, image_file)
    output_path = os.path.join(output_dir, image_file)

    # Load the binary image
    binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define the cropping coordinates (adjust these as needed)
    left, top, right, bottom = 262, 600, 4500, 5460
    cropped_image = binary_image[top:bottom, left:right]

    # Save the cropped image with the same filename in the output directory
    cv2.imwrite(output_path, cropped_image)

print("Cropping and saving completed.")
