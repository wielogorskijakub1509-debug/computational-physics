import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

walkers = 10000
limit_max = 250
limit_min = -250
x = np.zeros(walkers)
y = np.zeros(walkers)
D_history = []
time_history = []
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 6))
def update(frame):
    directions = np.random.randint(0, 4, size = walkers)
    x_step = np.zeros(walkers)
    y_step = np.zeros(walkers)
    x_step[directions == 0] = 1
    x_step[directions == 1] = -1
    y_step[directions == 2] = 1
    y_step[directions == 3] = -1
    global x, y, D_history, time_history
    x += x_step
    y += y_step
    distances_squared = x**2 + y**2
    mean_r_squared = np.mean(distances_squared)
    if frame > 0:
        D = mean_r_squared / (4 * (frame + 1))
    else:
        D = 0
    D_history.append(D)
    time_history.append(frame + 1)
    ax1.clear()
    ax1.hist2d(x, y, bins = 125, range = [[limit_min, limit_max], [limit_min, limit_max]], cmap = "hot")
    ax1.set_title(f"Random Walkers Simulation - Diffusion Coefficient D = {D :.5f}")
    ax1.set_xlim(limit_min, limit_max)
    ax1.set_ylim(limit_min, limit_max)
    ax2.clear()
    ax2.plot(time_history, D_history, color = "blue")
    ax2.axhline(0.25, color = "red", linestyle = "--", label = "Theoretical D = 0.25")
    ax2.set_title("Diffusion Coefficient D Over Time")
    ax2.set_xlabel("Time Steps")
    ax2.set_ylabel("Diffusion Coefficient D")


ani = anim.FuncAnimation(plt.gcf(), update, frames = 5000, interval = 40, repeat = False)
plt.show()
