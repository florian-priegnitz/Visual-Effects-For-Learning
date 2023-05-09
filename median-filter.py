import numpy as np
from scipy.ndimage import median_filter
from PIL import Image

# Prompt user for input image path
input_image_path = input("Bitte geben Sie den Bildpfad an: ")

# Load input image
input_image = Image.open(input_image_path).convert("L")
input_array = np.array(input_image)

# Apply median filter
window_size = 3
output_array = median_filter(input_array, size=window_size)

# Save output image
output_image = Image.fromarray(output_array)
output_image.save("median-filter.jpg")