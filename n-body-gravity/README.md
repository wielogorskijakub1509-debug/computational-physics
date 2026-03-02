# N-Body Gravity Simulation

Simulates the motion of multiple bodies interacting through Newtonian gravity in 2D. Users can define:

- Number of particles
- Masses
- Initial positions and velocities

Trajectories are visualized in real-time using Matplotlib.

---

## Run

```bash
cd n-body-gravity
python n_body.py
```

---

## How It Works

- Each particle experiences a gravitational force from every other particle.
- The forces are summed and used to calculate acceleration: `a = F/m`.
- Velocities and positions are updated using **Euler integration**:

```python
v_new = v_old + a*dt
x_new = x_old + v_new*dt
```

- Time is advanced in steps of `dt` seconds per frame, and trajectories are animated using Matplotlib.

---

## Limitations

There is a slight limitation of this programme with the fact that it uses Euler integration which will unfortunately lead to energy drift over long simulations. This could be a future improvement consideration by implementing another method of integration such as leapfrog or RK4.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install with:

```bash
pip install numpy matplotlib
```

---

## Skills Demonstrated

- Python programming
- NumPy for numerical calculations
- Matplotlib for animation and visualization
- Classical mechanics (Newtonian gravity)
- Vector-based force computation
- Numerical integration of differential equations

---

## Contact

Email: wielogorskijakub1509@gmail.com
