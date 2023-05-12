import numpy as np
import matplotlib.pyplot as plt

def rotate_points(points, angle, center, distance):
    # Winkel in Radiant umwandeln
    angle_rad = np.radians(angle)
    
    # Rotationsmatrix erstellen
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                                [np.sin(angle_rad), np.cos(angle_rad), 0],
                                [0, 0, 1]])
    
    # Transformationsmatrix erstellen
    transformation_matrix = np.array([[1, 0, distance * np.cos(angle_rad)],
                                      [0, 1, distance * np.sin(angle_rad)],
                                      [0, 0, 1]])
    
    # Zentrierungsmatrix erstellen
    center_matrix = np.array([[1, 0, -center[0]],
                              [0, 1, -center[1]],
                              [0, 0, 1]])
    
    # Zurückverschiebungsmatrix erstellen
    translation_matrix = np.array([[1, 0, center[0]],
                                   [0, 1, center[1]],
                                   [0, 0, 1]])
    
    # Transformierte Punkte berechnen
    result = np.matmul(points, translation_matrix.T @ transformation_matrix @ rotation_matrix.T @ center_matrix.T)
    return result

# Dreieckspunkte
A = np.array([1, 2, 1])
B = np.array([4, 4, 1])
C = np.array([2, 6, 1])

# Benutzereingabe für den Drehpunkt
center_x = float(input("Geben Sie die x-Koordinate des Drehpunkts ein: "))
center_y = float(input("Geben Sie die y-Koordinate des Drehpunkts ein: "))
center = np.array([center_x, center_y])

# Benutzereingabe für den Drehwinkel
angle = float(input("Geben Sie den Drehwinkel in Grad ein: "))

# Benutzereingabe für den Abstand zum Drehpunkt
distance = float(input("Geben Sie den Abstand zum Drehpunkt ein: "))

# Punkte in einer Matrix zusammenfassen
points = np.vstack((A, B, C))

# Dreieck um den angegebenen Punkt drehen
rotated_points = rotate_points(points, angle, center, distance)

# Original- und transformierte Punkte ausgeben
print("Originalpunkte:")
print(points[:, :2])
print("Rotierte Punkte:")
print(rotated_points[:, :2])

# Original- und transformierte Punkte plotten
fig, ax = plt.subplots()
ax.plot(*zip(*points[:, :2], points[0, :2]), label="Original", marker="o", linestyle="-", color="blue")
ax.plot(*zip(*rotated_points[:, :2], rotated_points[0, :2]), label="Transformiert (Rotation)", marker="o", linestyle="-", color="red")

# Punkte beschriften
for i, label in enumerate(["A", "B", "C"]):
    ax.text(points[i, 0], points[i, 1], label, fontsize=12, color="blue")
    ax.text(rotated_points[i, 0], rotated_points[i, 1], label + "' (Rotation)", fontsize=12, color="red")

ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis("equal")
ax.grid(True)

plt.show()

