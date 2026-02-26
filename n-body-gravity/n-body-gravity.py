import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

# Define a particle
class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype= float)
        self.velocity = np.array(velocity, dtype= float)
    
    def apply_force(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt
    
    def movement(self, dt):
        self.position += self.velocity * dt
    
#Get user input on particles:
n = int(input("How many particles? "))
particles = []
for i in range(n):
    print("Particle " + str(i+1) + ":")
    mass = float(input("Mass (Kg): "))
    x = float(input("Starting x position (m): "))
    y = float(input("Starting y position (m): "))
    vx = float(input("Starting velocity in x (m/s): "))
    vy = float(input("Starting velocity in y (m/s): "))
    
    p = Particle(mass=mass, position = [x, y], velocity = [vx, vy])
    particles.append(p)

# Find gravitational force
def gravty_getter(p1, p2, G):
    r_vector = p2.position - p1.position
    r = np.linalg.norm(r_vector)
    if r == 0:
        return np.array([0.0, 0.0])
    force_mag = (G * p1.mass * p2.mass) / r**2
    force_dir = r_vector / r
    force = force_mag * force_dir
    return force

# Calculate forces on particles
def calculate_forces(particles):
    forces = [np.array([0.0, 0.0]) for _ in particles]
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if i != j:
                force = gravty_getter(particles[i], particles[j], G = 6.67430e-11)
                forces[i] += force
                forces[j] -= force
    return forces

# Animation setup
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-1e11, 1e11)
ax.set_ylim(-1e11, 1e11)
ax.set_aspect('equal')
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')

scatter = ax.scatter([], [], s=100, c='blue')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Store position history for trails
trails = [[] for _ in particles]

time_elapsed = 0.0  # seconds, tracked across frames

def update(frame):
    global time_elapsed

    dt = 1e4 
    G = 6.67430e-11
    
    # Calculate forces and update particles
    forces = calculate_forces(particles)
    for i, particle in enumerate(particles):
        particle.apply_force(forces[i], dt)
        particle.movement(dt)
        trails[i].append(particle.position.copy())
    
    # Update scatter plot
    positions = np.array([p.position for p in particles])
    scatter.set_offsets(positions)
    
    # advance the cumulative time and display it
    time_elapsed += dt
    years = time_elapsed / (365.25 * 24 * 3600)
    time_text.set_text('Time: {:.2f} years'.format(years))
    
    return scatter, time_text

# Create animation
animation = anim.FuncAnimation(fig, update, frames=1000, interval=50, blit=True)
plt.show()
            
