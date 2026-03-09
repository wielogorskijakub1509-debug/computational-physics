# 2D Random Walk & Diffusion Simulation
This program simulates 10,000 random walkers on a 2D lattice, each taking steps in a random direction (up, down, left or right) at every time step. It produces a live animation showing the distribution of walkers and tracks the diffusion coefficient over time, verifying the Einstein diffusion relation.
## Physics Explanation
The simulation is built on the Einstein diffusion relation for 2D random walks:

⟨r²⟩ = 4Dt

Where ⟨r²⟩ is the mean squared displacement across all walkers, D is the diffusion coefficient, and t is the number of time steps. For a symmetric lattice random walk with unit step size, the theoretical value is D = 0.25. The simulation computes D at each frame from the ensemble average and converges to this value.
## Features
- 10,000 independent walkers evolved simultaneously using NumPy vectorisation
- Live two-panel animation: a 2D heatmap of walker positions and a plot of D(t) over time
- Emergent Gaussian spatial distribution visible as the simulation progresses
- Theoretical D = 0.25 shown as a reference line for comparison to data
## Usage
```bash
python random_walk.py
```
The animation runs automatically for 5,000 time steps. No input required.
## Software Requirements
- Python 3.x
- NumPy
- Matplotlib
## Possible Future Considerations
In the future, I could improve my simulation by: adding a 3D random walk variant, allowing variable step sizes or biased walks, or overlaying the theoretical Gaussian distribution for direct comparison with the simulated density.
