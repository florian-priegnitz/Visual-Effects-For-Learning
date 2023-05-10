import cv2
import numpy as np

def binary_threshold(gray_image, threshold=128):
    binary_image = np.zeros_like(gray_image, dtype=np.uint8)
    binary_image[gray_image >= threshold] = 255
    return binary_image

def red_green_mapping(gray_image, threshold=128):
    binary_image = binary_threshold(gray_image, threshold)
    color_image = np.zeros((gray_image.shape[0], gray_image.shape[1], 3), dtype=np.uint8)

    red_mask = binary_image == 0
    green_mask = binary_image == 255

    color_image[red_mask] = [0, 0, 255]  # Rote Farbe
    color_image[green_mask] = [0, 255, 0]  # Grüne Farbe

    return color_image

file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
red_green_image = red_green_mapping(input_image)

cv2.imwrite("red-green-spectrum-binary.jpg", red_green_image)
