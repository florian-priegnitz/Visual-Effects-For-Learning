import cv2

# Bildpfad vom Benutzer eingeben
file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

# b-Wert vom Benutzer eingeben
b = int(input("Bitte geben Sie den b-Wert für die Gray Level Mapping-Transformation ein: "))

# Bild in Graustufen lesen
input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

def apply_gray_scaling(image, b):
    return cv2.addWeighted(image, 1, image, 0, b)

# Gray Scaling-Bild mit b erstellen
gray_scaling_image = apply_gray_scaling(input_image, b)
cv2.imwrite("gray-scaling.jpg", gray_scaling_image)

# Gray Scaling-Bild mit b = -50 erstellen
gray_scaling_minus_50_image = apply_gray_scaling(input_image, -50)
cv2.imwrite("gray-scaling-50.jpg", gray_scaling_minus_50_image)

# Gray Scaling-Bild mit b = +50 erstellen
gray_scaling_plus_50_image = apply_gray_scaling(input_image, 50)
cv2.imwrite("gray-scaling+50.jpg", gray_scaling_plus_50_image)
