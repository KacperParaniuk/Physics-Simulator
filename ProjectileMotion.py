import numpy as np
import matplotlib.pyplot as plt

# Obtaining variables

v = 50 # inital velocity
theta = 45 # launch angle 
g = 9.81 # acceleration due to gravity 
flight_time = (2 * v * (np.sin(np.radians(theta))))/g
time_points = np.linspace(0,flight_time,500) # points in time on the parabola 

# calculating positions

theta_rad = np.radians(theta)
x = v * np.cos(theta_rad) * time_points # this will make an array of x points with each time point
y = v * np.sin(theta_rad) * time_points - .05 * g * time_points**2

# Plotting 

plt.figure(figsize=(10, 6))
plt.plot(x,y, label="Projectile Path")
plt.title("Projectile Motion", fontsize=14)
plt.xlabel("Horizontal Distance (m)", fontsize =12)
plt.ylabel("Vertical Distance (m)", fontsize =12)
plt.axhline(0,color='black', linewidth = 0.8, linestyle='--')
plt.legend
plt.grid
plt.show