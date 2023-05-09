import os
import cv2
import matplotlib.pyplot as plt

# Benutzer auffordern, den Bildpfad einzugeben
image_path = input("Bitte geben Sie den Pfad zum Bild ein: ")

# Bild laden
image = cv2.imread(image_path)

if image is not None:
    # Bild in Graustufen konvertieren
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Histogramm erstellen
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    # Histogramm plotten
    plt.figure()
    plt.title("Graustufen-Histogramm")
    plt.xlabel("Pixelintensität")
    plt.ylabel("Anzahl der Pixel")
    plt.plot(histogram)
    plt.xlim([0, 256])

    # Benutzer auffordern, den Ausgabepfad für das Histogramm anzugeben
    output_filename = "histogramm.png"
    output_path = os.path.join(os.getcwd(), output_filename)
    print("Das Histogramm wird unter folgendem Pfad gespeichert: ", output_path)

    # Histogramm speichern
    plt.savefig(output_path)

    # Optional: Histogramm anzeigen
    plt.show()
    print("Bild konnte geladen werden.")
else:
    print("Bild konnte nicht geladen werden. Bitte überprüfen Sie den Pfad.")
