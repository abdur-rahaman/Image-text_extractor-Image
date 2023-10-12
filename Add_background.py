from PIL import Image
import os

def addWhiteBackground(input_path, output_path):
    try:
        transparent_image = Image.open(input_path)
        image_width, image_height = transparent_image.size

        # Create a new white background image with the same dimensions
        white_background = Image.new("RGBA", (image_width, image_height), (255, 255, 255, 255))

        # Paste the transparent image onto the white background
        white_background.paste(transparent_image, (0, 0), transparent_image)

        # Save the resulting image with a white background
        white_background.save(output_path, "PNG")
        print(f"White background added to {input_path} and saved as {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Specify the input directory containing transparent images and the output directory
input_directory = "/media/la-belva/Riaz_disk/image_trans" #give your input file name
output_directory = "folder file" #give your file path

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List of input image files in the input directory
input_files = [f for f in os.listdir(input_directory) if f.endswith(".png")]

for input_file in input_files:
    input_path = os.path.join(input_directory, input_file)
    output_path = os.path.join(output_directory, input_file)
    addWhiteBackground(input_path, output_path)
