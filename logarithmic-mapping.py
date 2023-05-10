import cv2
import numpy as np

def logarithmic_mapping(image, c):
    image_normalized = image / 255.0
    log_mapped = c * np.log(1 + image_normalized)
    return (log_mapped * 255).astype(np.uint8)

file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")
c = float(input("Bitte geben Sie den Wert für c zwischen 0 und 1 ein: "))

input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

log_mapped_image = logarithmic_mapping(input_image, c)
cv2.imwrite("logarithmic-mapping.jpg", log_mapped_image)

log_mapped_image00 = logarithmic_mapping(input_image, 0)
cv2.imwrite("logarithmic-mapping00.jpg", log_mapped_image00)

log_mapped_image05 = logarithmic_mapping(input_image, 0.5)
cv2.imwrite("logarithmic-mapping05.jpg", log_mapped_image05)
