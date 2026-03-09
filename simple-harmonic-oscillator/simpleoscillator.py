import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
# Define particle
class Particle:
    def __init__(self, mass, position, velocity, k):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.k = k
    
    def calculate_force(self):
        return -self.k * self.position
    
    def update(self, dt):
        force = self.calculate_force()
        acceleration = force/self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

# get user input for parameters
mass = float(input("Mass (Kg): "))
k = float(input("Spring Constant (N/m): "))
x = float(input("Starting x position (m): "))

particle = Particle(mass = mass, position = x, velocity = 0.0, k = k)

# compute period and choose simulation parameters
if k <= 0:
    raise ValueError("Spring constant must be positive")
period = 2 * np.pi * np.sqrt(mass / k)
print(f"Computed period: {period:.3f} s")

# simulate for 5 cycles
cycles = 5
t_max = cycles * period
# time step small enough for smooth animation
dt = period / 200.0

# prepare the figure and artists for animation
fig, ax = plt.subplots()
# horizontal line for spring and point for mass
ax.set_xlim(-abs(x) * 1.5 - 0.1, abs(x) * 1.5 + 0.1)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])  # no vertical axis for a 1‑D oscillator
ax.set_xlabel("Position (m)")
ax.set_title("Simple Harmonic Oscillator")

mass_point, = ax.plot([], [], 'o', markersize=12, color='tab:blue')
spring_line, = ax.plot([], [], '-', lw=2, color='tab:gray')

# initialization function for FuncAnimation

def init():
    mass_point.set_data([], [])
    spring_line.set_data([], [])
    return mass_point, spring_line

# update function called for each frame

def update_frame(frame):
    particle.update(dt)
    pos = particle.position
    mass_point.set_data([pos], [0])
    spring_line.set_data([0, pos], [0, 0])
    return mass_point, spring_line

frames = int(np.ceil(t_max / dt))

ani = anim.FuncAnimation(
    fig,
    update_frame,
    frames=frames,
    init_func=init,
    blit=True,
    interval=dt * 1000  # milliseconds per frame
    repeat = False
)

plt.tight_layout()
plt.show()


