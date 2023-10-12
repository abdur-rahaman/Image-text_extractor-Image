from PIL import Image
import os

def removeTransparentBackground(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(output_path, "PNG")
    print(f"Transparent background removed for {input_path} and saved as {output_path}")

# Specify the directory containing the input images and where you want to save the output images
input_directory = "/media/la-belva/Riaz_disk/threshold_image"
output_directory = "/media/la-belva/Riaz_disk/image_trans"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
input_files = os.listdir(input_directory)

for input_file in input_files:
    if input_file.endswith(".jpg"):
        input_path = os.path.join(input_directory, input_file)
        output_path = os.path.join(output_directory, input_file.replace(".jpg", "_no_bg.png"))
        removeTransparentBackground(input_path, output_path)
