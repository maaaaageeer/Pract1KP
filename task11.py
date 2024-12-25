import pygame
import math

# Константы
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
COLOR_BACKGROUND = (20, 20, 40)
COLOR_AXES = (200, 50, 50)
COLOR_POLYGON = (100, 255, 100)
COLOR_TRANSFORMED_POLYGON = (50, 100, 200)

class CoordinateSystem:
    def __init__(self, origin, scale_x, scale_y):
        self.origin = origin
        self.scale_x = scale_x
        self.scale_y = scale_y

class OriginPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Scale:
    def __init__(self, pixels):
        self.pixels = pixels

def convert_x(coord_system, x):
    return int(coord_system.scale_x.pixels * x + coord_system.origin.x)

def convert_y(coord_system, y):
    return int(-coord_system.scale_y.pixels * y + coord_system.origin.y)

def draw_coordinate_axes(surface, coord_system, x_min, x_max, y_min, y_max, color):
    pygame.draw.line(surface, color, (convert_x(coord_system, x_min), convert_y(coord_system, 0)),
                     (convert_x(coord_system, x_max), convert_y(coord_system, 0)), 2)
    pygame.draw.line(surface, color, (convert_x(coord_system, 0), convert_y(coord_system, y_min)),
                     (convert_x(coord_system, 0), convert_y(coord_system, y_max)), 2)

def draw_polygon(surface, coord_system, points, color, thickness=2):
    screen_points = [(convert_x(coord_system, x), convert_y(coord_system, y)) for x, y in points]
    pygame.draw.polygon(surface, color, screen_points, thickness)

def initialize_matrix(rows, cols):
    return [[0.0 for _ in range(cols)] for _ in range(rows)]

def copy_matrix(src, dest):
    for i in range(len(src)):
        for j in range(len(src[i])):
            dest[i][j] = src[i][j]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Polygon Transform Overlay")
    clock = pygame.time.Clock()

    origin = OriginPoint(100, 650)
    scale_x = Scale(80)
    scale_y = Scale(80)
    coord_system = CoordinateSystem(origin, scale_x, scale_y)

    vertices = [[3.0, 1.0], [9.0, 1.0], [9.0, 7.0], [3.0, 7.0]]
    transformed_vertices = initialize_matrix(4, 2)

    shrink_factor = 0.90
    growth_factor = 1 - shrink_factor
    iterations = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_coordinate_axes(screen, coord_system, 0.0, 10.0, 0.0, 10.0, COLOR_AXES)

        for _ in range(iterations):
            draw_polygon(screen, coord_system, vertices, COLOR_POLYGON, 1)

            for i in range(len(vertices)):
                transformed_vertices[i][0] = shrink_factor * vertices[i][0] + growth_factor * vertices[(i + 1) % 4][0]
                transformed_vertices[i][1] = shrink_factor * vertices[i][1] + growth_factor * vertices[(i + 1) % 4][1]

            copy_matrix(transformed_vertices, vertices)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
