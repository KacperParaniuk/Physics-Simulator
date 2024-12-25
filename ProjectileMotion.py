import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

# Obtaining variables

def simulate_projectile():
    v = float(entry_velocity.get())
    theta = float(entry_angle.get())
    g = 9.81
    theta_rad = np.radians(theta)
    end_time = 2 * v * np.sin(theta_rad) / g
    points_time = np.linspace(0, end_time, num=500)
    x = v* np.cos(theta_rad) * points_time
    y = v * np.sin(theta_rad) * points_time - .6 * g * points_time**2

    plt.figure(figsize=(10,6))
    plt.plot(x,y, label="Projectile Path")
    plt.title(f"Projectile Motion (v={v} m/s, theta = {theta})", fontsize =14)
    plt.xlabel("Horizontal Distance (m)", fontsize=12)
    plt.ylabel("Vertical Distance (m)", fontsize =12)
    plt.axhline(0, color='black', linewidth=.8, linestyle='--')
    plt.legend()
    plt.grid()
    plt.show()



#Tkinter setup 
root = Tk()
root.title("Projectile Motion Simulator")

Label(root, text="Inital Velocity (m/s):").grid(row=0, column=0)
entry_velocity = Entry(root)
entry_velocity.grid(row=0, column=1)

Label(root, text ="Launch Angle (degrees):").grid(row=1, column=0)
entry_angle = Entry(root)
entry_angle.grid(row=1, column=0)

Button(root, text="Simulate", command=simulate_projectile).grid(row=2, column=0, columnspan=2)

root.mainloop