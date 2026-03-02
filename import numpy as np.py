import numpy as np
import matplotlib.pyplot as plt

# Vinklar (19 punkter från -90 till 90)
theta = np.arange(-90, 91, 10)

# Teoretiska värden (Malus lag)
I0 = 22  # mV
theta_rad = np.deg2rad(theta)
I_theory = I0 * np.cos(theta_rad)**2

# Uppmätta värden
I_measured = np.array([
    1.2, 1.5, 3.1, 5.0, 7.1, 9.5, 11.4, 12.9, 14.3,
    14.4,
    14.3, 13.1, 11.9, 9.6, 7.4, 5.2, 3.1, 1.9, 1.6
])

# Plot
plt.plot(theta, I_theory, 'o-', label="Malus lag (teori)")
plt.plot(theta, I_measured, 's-', label="Mätdata")

plt.xlim(-90, 90)
plt.xlabel("Vinkel (grader)")
plt.ylabel("Intensitet (mV)")
plt.title("Malus lag vs Mätdata")
plt.legend()
plt.grid(True)

plt.show()


# Vinklar 0–90°
theta = [20,25,30,35,40, 50, 60, 70, 80]
print(theta)

# Övre tabellen
Is = np.array([55, 50, 43.6, 38.3, 34.9, 25.7, 19.5, 15.7, 14.3])

# Undre tabellen
Ip = np.array([11.5, 4.1, 1.6, 0.8, 1.4, 7.1, 10.3, 12.6, 14.5])

# Plot
plt.plot(theta, Is, 'o-', label="S")
plt.plot(theta, Ip, 's-', label="P")

plt.xlim(0, 90)
plt.xlabel("Vinkel (grader)")
plt.ylabel("Intensitet (mV)")
plt.title("Två mätserier (0°–90°)")
plt.legend()
plt.grid(True)

plt.show()