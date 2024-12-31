import pygame
import sys
import numpy as np
from random import randint

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Projectile Motion")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)  
LIGHT_BLUE = (173,216,230)
BROWN = (150,75,0)


# clock for controlling frame rate
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

input_velocity = ""
input_angle = ""
active_input = None


# Projectile parameters
v0 = 0  # Initial velocity (pixels/second)
angle = 0  # Launch angle (degrees)
g = 9.81  # Gravity (pixels/second^2)
start_x, start_y = 50, HEIGHT - 50  # Initial position
x, y = start_x, start_y  # Current position
t = 0  # Time elapsed

angle_rad = np.radians(angle)

# Calculate initial velocity components
v0x = v0 * np.cos(angle_rad)
v0y = -v0 * np.sin(angle_rad)  # Negative because y decreases upwards in Pygame


velocity_box = pygame.Rect(50, 50, 200, 40)
angle_box = pygame.Rect(50, 110, 200, 40)
start_button = pygame.Rect(50, 180, 200, 50)

start = True
running = True
trajectory = []
simulation_running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # User input stuff! Add some interfaces that let the user know they are selected upon something
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if velocity_box.collidepoint(event.pos):
                active_input = "velocity"
            elif angle_box.collidepoint(event.pos):
                active_input = "angle"
            elif start_button.collidepoint(event.pos):
                try:
                    v0 = float(input_velocity)
                    angle = float(input_angle)
                    simulation_running = True # this is the boolean that sets the simulation to run.
                    trajectory = [] # Each time user gives a
                    # new input a new trajectory is given
                    t = 0 # time is also reset
                except ValueError:
                    print("Invalid input!")
                    simulation_running = False

            else:
                active_input = None

        if event.type == pygame.KEYDOWN and active_input:
            if event.key == pygame.K_BACKSPACE:
                if active_input =="velocity":
                    input_velocity = input_velocity[:-1]
                elif active_input =="angle":
                    input_angle = input_angle[:-1]
            elif event.key == pygame.K_RETURN and active_input:
                active_input = None
            else:
                if active_input == "velocity":
                    input_velocity+=event.unicode # takes the event (which is the key pressed) and converts it into string
                elif active_input == "angle":
                    input_angle +=event.unicode
    
    if simulation_running:
        
        t += 0.1
        angle_rad = np.radians(angle)
        v0x = v0 * np.cos(angle_rad) 
        v0y = -v0 * np.sin(angle_rad) 
        x = 50 + v0x * t 
        y = HEIGHT - 50 + v0y * t + 0.5 * g * t**2

        if start:
            h_max = (v0**2 * np.sin(angle_rad)**2) / (2 * g)  # Maximum height
            range_ = (v0**2 * np.sin(2 * angle_rad)) / g  # range
            start = False


        if y>=HEIGHT - 50:
            y = HEIGHT -50
            simulation_running = False

        trajectory.append((x,y))

    # Draw everything
    screen.fill(WHITE)  # Clear the screen
    pygame.draw.rect(screen, GRAY, velocity_box,2)
    pygame.draw.rect(screen, GRAY, angle_box, 2)
    pygame.draw.rect(screen, GRAY, start_button)
    pygame.draw.rect(screen, GREEN, (0, 550, 800, 25))
    pygame.draw.rect(screen, LIGHT_BLUE, (0,0,800,550))
    pygame.draw.rect(screen, BROWN, (0,575,800,550))



    # Draw input text
    velocity_text = font.render(input_velocity, True, BLACK)
    angle_text = font.render(input_angle, True, BLACK)
    start_text = font.render("Start Simulation", True, BLACK)
    screen.blit(velocity_text, (velocity_box.x + 10, velocity_box.y + 5))
    screen.blit(angle_text, (angle_box.x + 10, angle_box.y + 5))
    screen.blit(start_text, (start_button.x + 10, start_button.y + 10))

    # Draw labels
    velocity_label = font.render("Velocity (m/s):", True, BLACK)
    angle_label = font.render("Angle (°):", True, BLACK)
    screen.blit(velocity_label, (velocity_box.x, velocity_box.y - 30))
    screen.blit(angle_label, (angle_box.x, angle_box.y - 30))


    # Draw trajectory
    for point in trajectory:  # Draw the trajectory
        pygame.draw.circle(screen, BLUE, (int(point[0]), int(point[1])), 2)

    # Draw projectile
    if trajectory: # makes sure there are points in 2D array
        pygame.draw.circle(screen, RED, (int(trajectory[-1][0]), int(trajectory[-1][1])), 5)
        # or you can draw the projectile as the x and y's are being changed in this loop 
        # pygame.draw.circle(screen, RED, (int(x), int(y)), 5)  



    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
sys.exit()