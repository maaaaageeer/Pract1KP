import pygame
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
COLOR_LIGHT_GRAY = (240, 240, 240)  # Светло-серый фон
COLOR_DARK_RED = (139, 0, 0)  # Темно-красный
COLOR_TEAL = (0, 128, 128)  # Бирюзовый
COLOR_ORANGE = (255, 140, 0)  # Оранжевый

REFLECTION_MATRIX = np.array([[0, 1], [1, 0]])
TRIANGLE_VERTICES = np.array([[8, 1], [7, 3], [6, 2]], dtype=float)

def apply_transformation(vertices, matrix):
    transformed_vertices = np.dot(vertices, matrix)
    return transformed_vertices

def render_triangle(surface, origin, color, vertices, scale):
    screen_coordinates = [
        (int(point[0] * scale + origin[0]), int(origin[1] - point[1] * scale))
        for point in vertices
    ]
    pygame.draw.polygon(surface, color, screen_coordinates, 3)

def main():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Reflecting a Triangle")
    display.fill(COLOR_LIGHT_GRAY)

    origin_x = WINDOW_WIDTH / 2
    origin_y = WINDOW_HEIGHT / 2
    origin = np.array([origin_x, origin_y])

    scaling = 20

    reflected_triangle = apply_transformation(TRIANGLE_VERTICES, REFLECTION_MATRIX)

    render_triangle(display, origin, COLOR_ORANGE, TRIANGLE_VERTICES, scaling)
    render_triangle(display, origin, COLOR_TEAL, reflected_triangle, scaling)

    pygame.display.update()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

    pygame.quit()

if __name__ == "__main__":
    main()
