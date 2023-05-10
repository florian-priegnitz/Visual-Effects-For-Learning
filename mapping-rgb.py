import cv2
import numpy as np

def red_green_mapping(gray_image):
    color_image = np.zeros((gray_image.shape[0], gray_image.shape[1], 3), dtype=np.uint8)
    color_image[:, :, 0] = gray_image
    color_image[:, :, 1] = gray_image
    return color_image

file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

red_green_image = red_green_mapping(input_image)
cv2.imwrite("red-green-spectrum.jpg", red_green_image)

only_red_image = np.zeros_like(red_green_image)
only_red_image[:, :, 0] = input_image
cv2.imwrite("only-red-spectrum.jpg", only_red_image)

only_green_image = np.zeros_like(red_green_image)
only_green_image[:, :, 1] = input_image
cv2.imwrite("only-green-spectrum.jpg", only_green_image)

only_blue_image = np.zeros_like(red_green_image)
only_blue_image[:, :, 2] = input_image
cv2.imwrite("only-blue-spectrum.jpg", only_blue_image)
