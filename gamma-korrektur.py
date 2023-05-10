import cv2
import numpy as np

# Bildpfad vom Benutzer eingeben
file_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

# Gamma-Wert vom Benutzer eingeben
gamma = float(input("Bitte geben Sie den gewünschten Gamma-Wert ein: "))

# Bild lesen
input_image = cv2.imread(file_path)

# Gamma-Korrektur-Funktion
def apply_gamma_correction(image, gamma_value):
    # Bild normalisieren
    image_normalized = image / 255.0

    # Gamma-Korrektur anwenden
    corrected_image = np.power(image_normalized, gamma_value)

    # Bild auf den Wertebereich 0-255 zurück skalieren
    corrected_image_scaled = (corrected_image * 255).astype(np.uint8)
    
    return corrected_image_scaled

# Gamma-Korrektur für das vom Benutzer eingegebene Gamma anwenden
gamma_corrected_image = apply_gamma_correction(input_image, gamma)
cv2.imwrite("gamma-korrektur.jpg", gamma_corrected_image)

# Gamma-Korrektur für Gamma-Wert 0.8 anwenden
gamma_corrected_image08 = apply_gamma_correction(input_image, 0.8)
cv2.imwrite("gamma-korrektur08.jpg", gamma_corrected_image08)

# Gamma-Korrektur für Gamma-Wert 2.2 anwenden
gamma_corrected_image22 = apply_gamma_correction(input_image, 2.2)
cv2.imwrite("gamma-korrektur22.jpg", gamma_corrected_image22)
