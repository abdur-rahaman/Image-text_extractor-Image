# import numpy as np
# import pytesseract
# import argparse
# import imutils
# import matplotlib.pyplot as plt
# from PIL import Image
# import pytesseract

import os
import cv2

# Source and destination directories
source_dir = '/media/la-belva/Riaz_disk/1850-1899 - full mushaf'
destination_dir = '/media/la-belva/Riaz_disk/threshold_image'

# Make sure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        # Construct the full path to the source image
        source_image_path = os.path.join(source_dir, filename)

        # Read the image
        image = cv2.imread(source_image_path)

        # Process the image (your existing code here)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 160, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # Invert the mask (text regions will be white)
        text_mask = cv2.bitwise_not(thresh)

        # Apply the mask to the original image to keep only the text
        result_image = cv2.bitwise_and(image, image, mask=thresh)

        # Save the result image to the destination directory
        destination_image_path = os.path.join(destination_dir, filename)
        cv2.imwrite(destination_image_path, text_mask)
