# Projectile Motion Simulator

This program will take in user input on two parameters: initial velocity and angle of launch. Running the program will output a parabola resembling the path taken by a particle which has those parameters.

## Physics explanation

The simulation uses the standard kinematic equations for projectile motion:

- **Horizontal position:** x(t) = v₀cos(θ)t
- **Vertical position:** y(t) = v₀sin(θ)t - ½gt²
- **Time of flight:** t = 2v₀sin(θ)/g

Where:
- v₀ = initial velocity (m/s)
- θ = launch angle (degrees)
- g = 9.8 m/s² (gravitational acceleration)

## Features

- User input for initial velocity and launch angle
- Plots trajectory using NumPy and Matplotlib
- Automatically stops at ground level (y = 0)
- Shows labeled axes with units

## Usage
```bash
python projectile.py
```

Enter initial velocity and launch angle when prompted.

## Example Output

Launch a projectile at 50 m/s at 45° to see a parabolic trajectory.

## Software Requirements

- Python 3.x
- NumPy
- Matplotlib

## Possible Future Considerations

My program could be improved in the future by: adding air resistance, showing values for range and max height and/or allowing the user to have inputs for multiple particles for the sake of comparison