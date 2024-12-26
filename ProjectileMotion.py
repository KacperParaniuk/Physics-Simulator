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


def simulate_projectile_drag():
    v = float(entry_velocity.get())
    theta = float(entry_angle.get())
    m = float(mass.get())
    a = float(area.get())
    dt = 0.01 # time step
    g = 9.81
    theta_rad = np.radians(theta)
    density_of_air = 1.225 # kg/m^3
    drag_coeff = 0.47

    vx = v * np.cos(theta_rad)
    vy = v * np.sin(theta_rad)

    x, y = 0, 0 # initial position of object 
    x_values = [x] # will be all the values in parabola that are modified by drag
    y_values = [y] # y - values modified by drag 

    # time loop because a lot of variables are dependent upon each other
    while y >= 0:
        v = np.sqrt(vx**2 + vy**2)
        ax = -.5 * density_of_air * vx**2 * drag_coeff * a / m
        ay = -g - .5 * density_of_air *vy**2 * drag_coeff * a / m
        vx = vx + ax*dt
        vy = vy + ay*dt
        x += vx*dt
        y += vy*dt
        x_values.append(x)
        y_values.append(y)
        


    plt.figure(figsize=(10,6))    
    plt.plot(x_values,y_values, label="Projectile Path")
    plt.title(f"Projectile Motion (v={v} m/s, theta = {theta})", fontsize =14)
    plt.xlabel("Horizontal Distance (m)", fontsize=12)
    plt.ylabel("Vertical Distance (m)", fontsize =12)
    plt.axhline(0, color='black', linewidth=.8, linestyle='--')
    plt.legend()
    plt.grid()
    plt.show()


def getDragVar():
    root2 = Tk()
    Label(root2, text="Area of Object (m^2)").grid(row=0, column=0) # m^2
    global area
    area = Entry(root2)
    area.grid(row=0, column=1)

    Label(root2, text="Mass of Object (kg)").grid(row=1, column=0) 
    global mass
    mass = Entry(root2)
    mass.grid(row=1, column=1)

    Button(root2, text="Simulate with drag", command=simulate_projectile_drag).grid(row=2, column=2, columnspan=1)


    root2.mainloop




#Tkinter setup 
root = Tk()
root.title("Projectile Motion Simulator")

Label(root, text="Initial Velocity (m/s):").grid(row=0, column=0)
entry_velocity = Entry(root)
entry_velocity.grid(row=0, column=1)

Label(root, text ="Launch Angle (degrees):").grid(row=1, column=0)
entry_angle = Entry(root)
entry_angle.grid(row=1, column=1)

Button(root, text="Simulate w/o drag", command=simulate_projectile).grid(row=2, column=0, columnspan=1)
Button(root, text="Simulate with drag", command=getDragVar).grid(row=2, column=1, columnspan=1)


root.mainloop()