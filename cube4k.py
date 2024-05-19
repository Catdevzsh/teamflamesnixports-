import pygame
import sys
import numpy as np
import time

# Initialize Pygame
pygame.init()

# Define the window size
window_width, window_height = 600, 400

# Set up the display
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('PS1 Logo with 3D Spinning Cube')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Function to display the BIOS loader screen
def bios_loader():
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('PS1DREAM 1.0', True, WHITE)
    screen.blit(text, (window_width // 2 - text.get_width() // 2, window_height // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)

# Function to draw the PS1 logo pixel by pixel
def draw_ps1_logo(surface):
    # Draw the PS1 logo using polygons
    pygame.draw.polygon(surface, BLUE, [(50, 50), (70, 50), (60, 90)])
    pygame.draw.polygon(surface, RED, [(70, 50), (90, 70), (60, 90)])
    pygame.draw.polygon(surface, YELLOW, [(50, 50), (60, 90), (30, 70)])
    pygame.draw.polygon(surface, GREEN, [(30, 70), (60, 90), (40, 110)])

# Define the vertices of a cube in 2D
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Define the edges of a cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

def draw_cube(vertices, screen, color=WHITE):
    for edge in edges:
        points = []
        for vertex in edge:
            x = vertices[vertex][0]
            y = vertices[vertex][1]
            z = vertices[vertex][2]

            # Fake 3D projection
            f = 200 / (z + 5)
            x, y = x * f, y * f

            points.append((window_width // 2 + int(x), window_height // 2 + int(y)))

        pygame.draw.line(screen, color, points[0], points[1], 1)

def rotate(vertices, angle_x, angle_y):
    rotation_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])

    rotation_y = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])

    return np.dot(vertices, np.dot(rotation_x, rotation_y))

# Show the BIOS loader screen
bios_loader()

# Main loop
angle_x, angle_y = 0, 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_ps1_logo(screen)

    rotated_vertices = rotate(vertices, angle_x, angle_y)
    draw_cube(rotated_vertices, screen)

    angle_x += 0.01
    angle_y += 0.01

    pygame.display.flip()
    clock.tick(60)
