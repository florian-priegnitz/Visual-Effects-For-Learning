import cv2
import numpy as np

def main():
    file_path = input("Bitte geben Sie den Bildpfad an: ")
    input_image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    
    sigma = float(input("Bitte geben Sie die Standardabweichung (Sigma) zwischen 0.5-5 an für den Gauß-Filter ein. 0.5 wäre sehr leichte Weichzeichnung, ideal für Bilder mit feinen Details und geringem Rauschen während sehr starke Weichzeichnung, ideal für die Glättung großer Strukturen oder die Erzeugung von künstlerischen Effekten: "))
    kernel_size = int(6 * sigma + 1)  # Empfohlene Größe des Filterkerns basierend auf Sigma

    # Stelle sicher, dass die Kernelgröße ungerade ist
    if kernel_size % 2 == 0:
        kernel_size += 1

    output_image = cv2.GaussianBlur(input_image, (kernel_size, kernel_size), sigma)

    cv2.imwrite("gauss-filter.jpg", output_image)
    print("Das gefilterte Bild wurde als 'gauss-filter.jpg' gespeichert.")

if __name__ == "__main__":
    main()
