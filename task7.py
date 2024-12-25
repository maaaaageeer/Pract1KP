import pygame
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
COLOR_LIGHT_GRAY = (240, 240, 240)  # Светло-серый фон
COLOR_DARK_BLUE = (0, 0, 139)  # Темно-синий
COLOR_ORANGE = (255, 140, 0)  # Оранжевый
COLOR_PURPLE = (128, 0, 128)  # Фиолетовый

ROTATION_MATRIX = np.array([[0, 1], [-1, 0]])
TRIANGLE_COORDS = np.array([[3, -1], [4, 1], [2, 1]], dtype=float)

def rotate_triangle(vertices, rotation_matrix):
    return np.dot(vertices, rotation_matrix)

def render_triangle(surface, origin, color, vertices):
    coordinates = [(int(vertex[0] + origin[0]), int(origin[1] - vertex[1])) for vertex in vertices]
    pygame.draw.polygon(surface, color, coordinates, 3)

def main():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Rotating a Triangle")
    display.fill(COLOR_LIGHT_GRAY)

    origin_x = WINDOW_WIDTH / 2
    origin_y = WINDOW_HEIGHT / 2
    origin = np.array([origin_x, origin_y])

    scaling_factor = 100
    offset_x = -100
    offset_y = -100

    scaled_triangle = TRIANGLE_COORDS * scaling_factor
    scaled_triangle[:, 0] += offset_x
    scaled_triangle[:, 1] += offset_y

    rotated_triangle = rotate_triangle(scaled_triangle, ROTATION_MATRIX)

    rotated_triangle[:, 0] += offset_x
    rotated_triangle[:, 1] += offset_y

    render_triangle(display, origin, COLOR_ORANGE, scaled_triangle)
    render_triangle(display, origin, COLOR_PURPLE, rotated_triangle)

    pygame.display.update()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
