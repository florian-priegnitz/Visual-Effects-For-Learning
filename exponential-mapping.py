import cv2
import numpy as np

def exponential_mapping(image, c):
    image_normalized = image / 255.0
    exp_mapped = c * (np.exp(image_normalized) - 1)
    return (exp_mapped * 255).astype(np.uint8)

file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")
c = float(input("Bitte geben Sie den Wert für c zwischen 0 und 1 ein: "))

input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

exp_mapped_image = exponential_mapping(input_image, c)
cv2.imwrite("exponential-mapping.jpg", exp_mapped_image)

exp_mapped_image00 = exponential_mapping(input_image, 0)
cv2.imwrite("exponential-mapping00.jpg", exp_mapped_image00)

exp_mapped_image05 = exponential_mapping(input_image, 0.5)
cv2.imwrite("exponential-mapping05.jpg", exp_mapped_image05)
