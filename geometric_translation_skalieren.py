import numpy as np
import matplotlib.pyplot as plt

def scale_points(points, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0, 0],
                               [0, scale_factor, 0],
                               [0, 0, 1]])
    # Transformierte Punkte ausgeben
    print("Skalierungsmatrix:")
    print(scaling_matrix[:, :3])
    result = np.matmul(points, scaling_matrix.T)
    return result

# Dreieckspunkte
A = np.array([1, 2, 1])
B = np.array([4, 4, 1])
C = np.array([2, 6, 1])

# Skalierungsfaktor für Vergrößerung
scale_factor_enlarge = 2

# Skalierungsfaktor für Verkleinerung
scale_factor_reduce = 0.5

# Punkte in einer Matrix zusammenfassen
points = np.vstack((A, B, C))

# Transformierte Punkte berechnen - Vergrößerung
scaled_points_enlarge = scale_points(points, scale_factor_enlarge)

# Transformierte Punkte berechnen - Verkleinerung
scaled_points_reduce = scale_points(points, scale_factor_reduce)

# Original- und transformierte Punkte ausgeben
print("Originalpunkte:")
print(points[:, :3])
print("Vergrößerte Punkte:")
print(scaled_points_enlarge[:, :3])
print("Verkleinerte Punkte:")
print(scaled_points_reduce[:, :3])

# Original- und transformierte Punkte plotten
fig, ax = plt.subplots()
ax.plot(*zip(*points[:, :2], points[0, :2]), label="Original", marker="o", linestyle="-", color="blue")
ax.plot(*zip(*scaled_points_enlarge[:, :2], scaled_points_enlarge[0, :2]), label="Vergrößerung (VG)", marker="o", linestyle="-", color="red")
ax.plot(*zip(*scaled_points_reduce[:, :2], scaled_points_reduce[0, :2]), label="Verkleinerung (VK)", marker="o", linestyle="-", color="green")

# Punkte beschriften
for i, label in enumerate(["A", "B", "C"]):
    ax.text(points[i, 0], points[i, 1], label, fontsize=12, color="blue")
    ax.text(scaled_points_enlarge[i, 0], scaled_points_enlarge[i, 1], label + "' (VG)", fontsize=12, color="red")
    ax.text(scaled_points_reduce[i, 0], scaled_points_reduce[i, 1], label + "'' (VK)", fontsize=12, color="green")

ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.axis("equal")
ax.grid(True)

plt.show()
