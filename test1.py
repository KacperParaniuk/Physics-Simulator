import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Virtual surface dimensions
VIRTUAL_WIDTH, VIRTUAL_HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))  # Actual screen
virtual_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))  # Virtual surface

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Projectile parameters
v0 = 100  # Initial velocity (pixels/second)
angle = 45  # Launch angle (degrees)
g = 9.81  # Gravity (pixels/second^2)

# Convert angle to radians
angle_rad = math.radians(angle)

# Initial position and velocity
start_x, start_y = 50, VIRTUAL_HEIGHT - 50
x, y = start_x, start_y
t = 0
trajectory = []

# Variables for trajectory bounds
max_x = start_x
max_y = start_y

# Run the simulation to calculate bounds
while True:
    t += 0.1
    x = start_x + v0 * math.cos(angle_rad) * t
    y = start_y - (v0 * math.sin(angle_rad) * t - 0.5 * g * t**2)

    if y >= VIRTUAL_HEIGHT - 50:  # Stop when the projectile hits the ground
        break

    trajectory.append((x, y))
    max_x = max(max_x, x)
    max_y = min(max_y, y)  # Smaller y because the origin (0,0) is at the top-left

# Calculate scaling and offsets
trajectory_width = max_x - start_x
trajectory_height = start_y - max_y

# Zoom level to fit the trajectory
zoom_level_x = VIRTUAL_WIDTH / trajectory_width
zoom_level_y = VIRTUAL_HEIGHT / trajectory_height
zoom_level = min(zoom_level_x, zoom_level_y)  # Use the smaller zoom level to fit both dimensions

# Offset to center the trajectory on the screen
offset_x = start_x - trajectory_width / 2
offset_y = (start_y + max_y) / 2

# Reset for simulation
x, y = start_x, start_y
t = 0
simulation_running = True

# Run the simulation with fitted zoom
while simulation_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation_running = False

    # Update physics
    t += 0.1
    x = start_x + v0 * math.cos(angle_rad) * t
    y = start_y - (v0 * math.sin(angle_rad) * t - 0.5 * g * t**2)

    # Stop if the projectile hits the ground
    if y >= VIRTUAL_HEIGHT - 50:
        y = VIRTUAL_HEIGHT - 50
        simulation_running = False

    # Draw everything to the virtual surface
    virtual_surface.fill(WHITE)
    pygame.draw.circle(virtual_surface, RED, (int(x), int(y)), 5)  # Projectile
    for point in trajectory:
        pygame.draw.circle(virtual_surface, BLUE, (int(point[0]), int(point[1])), 2)

    # Scale and blit the virtual surface to the actual screen
    scaled_surface = pygame.transform.smoothscale(
        virtual_surface,
        (int(VIRTUAL_WIDTH * zoom_level), int(VIRTUAL_HEIGHT * zoom_level))
    )

    # Center the trajectory on the screen
    screen.fill(WHITE)
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
