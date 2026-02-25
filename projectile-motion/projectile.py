import numpy as np
import matplotlib.pyplot as plt
# Get parameters from user with exception handling
while True:
    try:
        v0 = float(input("What is the initial velocity in m/s? "))
        angle = float(input("What is the angle of launch in degrees? "))
        break
    except ValueError:
        pass
g = 9.8
theta = np.radians(angle)
# Work out time of flight from user parameters
t_flight = (2 * v0 * np.sin(theta)) / g
# Set up time array
t_array = np.linspace(0, t_flight, 100)
# Calculate positions
x = v0 * t_array * np.cos(theta)
y = (v0 * t_array * np.sin(theta)) - (0.5 * g * t_array**2)
# Set to only be above ground using masking
mask = y >= 0
x = x[mask]
y = y[mask]
# Plot result
plt.plot(x, y)
plt.title(f"Projectile motion (v_0 = {v0}m/s, Angle of launch = {angle} degrees)")
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.axis("equal")
plt.show()
#test change