import numpy as np
from PIL import Image

def korrelationsfilter(eingabe_bild, kernel):
    input_array = np.array(eingabe_bild)
    output_array = np.zeros(input_array.shape, dtype=np.float32)

    kernel_height, kernel_width = kernel.shape
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    gepolstertes_eingabe_bild = np.pad(input_array, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    for x in range(input_array.shape[0]):
        for y in range(input_array.shape[1]):
            output_array[x, y] = np.sum(gepolstertes_eingabe_bild[x:x+kernel_height, y:y+kernel_width] * kernel)

    return Image.fromarray(output_array.astype(np.uint8))

bildpfad = input("Bitte geben Sie den Pfad zum Bild ein: ")
eingabe_bild = Image.open(bildpfad).convert("L")
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16.0  # Gauß'scher Weichzeichner-Filterkernel
ausgabe_bild = korrelationsfilter(eingabe_bild, kernel)
ausgabe_bild.save("correlation-filter.jpg")
