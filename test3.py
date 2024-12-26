from tkinter import Tk, Label, Entry

root = Tk()
root.title("Projectile Motion Simulator")

Label(root, text="Inital Velocity (m/s):").grid(row=0, column=0)
entry_velocity = Entry(root)
entry_velocity.grid(row=0, column=1)

Label(root, text ="Launch Angle (degrees):").grid(row=1, column=0)
entry_angle = Entry(root)
entry_angle.grid(row=1, column=0)


root.mainloop