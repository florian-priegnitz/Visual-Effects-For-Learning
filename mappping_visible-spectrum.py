import cv2

def apply_colormap(gray_image, colormap=cv2.COLORMAP_JET):
    return cv2.applyColorMap(gray_image, colormap)

file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

colored_image = apply_colormap(input_image)
cv2.imwrite("visible-spectrum.jpg", colored_image)
