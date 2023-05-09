import cv2
import numpy as np

def harris_corner_detector(img, k=0.04, threshold=0.01):
    # Convert the image to grayscale if it is in color
    if len(img.shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. Calculate derivatives
    Ix = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    Iy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    # 2. Compute the covariance matrix
    Ix2 = Ix ** 2
    Iy2 = Iy ** 2
    Ixy = Ix * Iy

    kernel = cv2.getGaussianKernel(3, 1.5)
    Sx2 = cv2.sepFilter2D(Ix2, -1, kernel, kernel)
    Sy2 = cv2.sepFilter2D(Iy2, -1, kernel, kernel)
    Sxy = cv2.sepFilter2D(Ixy, -1, kernel, kernel)

    # 3. Compute the corner strength
    detCov = Sx2 * Sy2 - Sxy ** 2
    traceCov = Sx2 + Sy2
    corner_strength = detCov - k * traceCov ** 2

    # 4. Find corners
    corner_map = np.zeros_like(img)
    corner_map[corner_strength > threshold * corner_strength.max()] = 255

    return corner_map

# Ask user for image file path
image_path = input("Bitte geben Sie den Pfad zur Bilddatei ein: ")

# Load the image
img = cv2.imread(image_path)

# Ask user for threshold value
threshold = float(input("Bitte geben Sie den Schwellenwert für die Eckenstärke ein (z.B. 0.01): "))

# Apply Harris corner detection
corners = harris_corner_detector(img, threshold=threshold)

# Save the result
output_filename = "harris-ecken-detektor.jpg"
cv2.imwrite(output_filename, corners)