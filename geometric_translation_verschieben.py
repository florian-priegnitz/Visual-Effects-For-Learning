import numpy as np
import matplotlib.pyplot as plt

def translate_points(points, dx, dy):
    translation_matrix = np.array([[1, 0, dx],
                                   [0, 1, dy],
                                   [0, 0, 1]])
    # Transformierte Punkte ausgeben
    print("Translationsmatrix:")
    print(translation_matrix[:, :3])
    result = np.matmul(points, translation_matrix.T)
    return result

# Dreieckspunkte
A = np.array([1, 2, 1])
B = np.array([4, 4, 1])
C = np.array([2, 6, 1])

# Verschiebung: 3 nach links, 4 nach oben
dx = -3
dy = 4

# Punkte in einer Matrix zusammenfassen
points = np.vstack((A, B, C))

# Transformierte Punkte berechnen
translated_points = translate_points(points, dx, dy)

# Original- und transformierte Punkte ausgeben
print("Originalpunkte:")
print(points[:, :3])

# Addieren der Transformationsmatrix zur Originalmatrix
print("Addieren der Transformationsmatrix zur Originalmatrix:")
print(points[:, :3] + np.array([dx, dy]))

# Original- und transformierte Punkte plotten
fig, ax = plt.subplots()
ax.plot(*zip(*points[:, :2], points[0, :2]), label="Original", marker="o", linestyle="-", color="blue")
ax.plot(*zip(*translated_points[:, :2], translated_points[0, :2]), label="Transformiert", marker="o", linestyle="-", color="red")

# Punkte beschriften
for i, label in enumerate(["A", "B", "C"]):
    ax.text(points[i, 0], points[i, 1], label, fontsize=12, color="blue")
    ax.text(translated_points[i, 0], translated_points[i, 1], label + "'", fontsize=12, color="red")

ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis("equal")
ax.grid(True)

plt.show()

