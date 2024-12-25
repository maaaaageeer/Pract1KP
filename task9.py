import pygame
import numpy as np

# Параметры экрана
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 650
COLOR_BACKGROUND = (240, 248, 255)  # Светло-голубой фон
COLOR_OUTLINE1 = (255, 165, 0)  # Оранжевый для исходного треугольника
COLOR_OUTLINE2 = (72, 209, 204)  # Средний бирюзовый для масштабированного треугольника

# Матрица масштабирования
TRANSFORMATION_MATRIX = np.array([[2, 0], [0, 2]])

# Координаты исходного треугольника
TRIANGLE_VERTICES = np.array([[5, 1], [5, 2], [3, 2]], dtype=float)


def apply_matrix(vertices, matrix):
    return np.dot(vertices, matrix)


def draw_triangle(surface, center, color, vertices):
    points = [(int(vertex[0] + center[0]), int(center[1] - vertex[1])) for vertex in vertices]
    pygame.draw.polygon(surface, color, points, 3)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Triangle Scaling Visualization")
    screen.fill(COLOR_BACKGROUND)

    center_x = WINDOW_WIDTH / 2
    center_y = WINDOW_HEIGHT / 2
    center = np.array([center_x, center_y])

    scale = 50
    offset_x = -150
    offset_y = -70

    original_triangle = TRIANGLE_VERTICES * scale
    original_triangle[:, 0] += offset_x
    original_triangle[:, 1] += offset_y

    transformed_triangle = apply_matrix(TRIANGLE_VERTICES, TRANSFORMATION_MATRIX)
    transformed_triangle *= scale
    transformed_triangle[:, 0] += offset_x
    transformed_triangle[:, 1] += offset_y

    draw_triangle(screen, center, COLOR_OUTLINE1, original_triangle)
    draw_triangle(screen, center, COLOR_OUTLINE2, transformed_triangle)

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
