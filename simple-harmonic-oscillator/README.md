# Simple Harmonic Oscillator (1D)

This folder contains a minimal Python program that simulates and animates
a one‑dimensional mass attached to a spring obeying Hooke’s law. The
animation is created using `matplotlib` and illustrates the classic
sinusoidal motion of a simple harmonic oscillator.

## Features

* Real‑time animation of a point mass moving on a horizontal axis.
* Adjustable mass, spring constant, and initial displacement via command‑line
  prompts.
* Automatic calculation of the natural period and simulation for several
  oscillation cycles.
* Uses a basic Euler integration step for the dynamics (sufficient for
  illustrative purposes).

## Requirements

* Python 3.8 or later
* `numpy`
* `matplotlib`

Install dependencies with:

```bash
pip install numpy matplotlib
```

## Usage

Navigate to this directory and run the script:

```bash
python simpleoscillator.py
```

You will be prompted to enter the mass (kg), spring constant (N/m), and
starting position (m). After entering the values, a window will open showing
the spring and mass oscillating for a few periods.

### Example session

```
Mass (Kg): 1
Spring Constant (N/m): 10
Starting x position (m): 0.1
Computed small‑oscillation period: 1.987 s
```

A new window displays the animation; close it to exit the program.

## How it works

The script defines a `Particle` class that stores the state of the mass and
updates its position and velocity using the force `F = -k x`. The class
records the position history (which may be useful for later plotting).

The animation uses `matplotlib.animation.FuncAnimation`:

1. An `init()` function clears the plot.
2. An `update_frame()` function advances the particle by a fixed timestep and
   updates the `Line2D` objects representing the mass and spring.
3. `FuncAnimation` calls these repeatedly, with `blit=True` for efficiency.

The spring is rendered as a straight line from the fixed origin to the mass
point; the mass itself is a blue circle.

## Extending the project

Some ideas to experiment with:

* Add a more accurate integrator (e.g. Runge–Kutta).
* Display a trace of the motion or plot energy vs time.
* Save the animation to an MP4 or GIF file using `ani.save()`.
* Animate a vertical spring with gravity included.
