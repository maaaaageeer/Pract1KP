import pygame
import numpy as np

# Параметры окна и цвета
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800
COLOR_BACKGROUND = (240, 248, 255)  # Светло-голубой
COLOR_DARK_GRAY = (64, 64, 64)
COLOR_ORANGE = (255, 165, 0)
COLOR_LIGHT_GREEN = (144, 238, 144)
COLOR_DARK_BLUE = (0, 0, 139)
COLOR_PINK = (255, 105, 180)
COLOR_LAVENDER = (230, 230, 250)
TEXT_SIZE = 24

# Матрица преобразования и координаты отрезка
TRANSFORM_MATRIX = np.array([[1, 2], [3, 1]])
LINE_COORDS = np.array([[0, 100], [200, 300]], dtype=float)

def calculate_midpoint(line):
    return (line[0] + line[1]) / 2

def apply_transformation(line, matrix):
    return np.dot(line, matrix)

def draw_segment(surface, origin, color, start, end, thickness=4):
    x1, y1 = int(start[0] + origin[0]), int(origin[1] - start[1])
    x2, y2 = int(end[0] + origin[0]), int(origin[1] - end[1])
    pygame.draw.line(surface, color, (x1, y1), (x2, y2), thickness)

def draw_marker(surface, origin, color, pos, radius):
    x, y = int(pos[0] + origin[0]), int(origin[1] - pos[1])
    pygame.draw.circle(surface, color, (x, y), radius)

def render_text(surface, message, x, y, color=COLOR_DARK_GRAY):
    font = pygame.font.Font(None, TEXT_SIZE)
    text_surface = font.render(message, True, color)
    surface.blit(text_surface, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Line Transformation")
    screen.fill(COLOR_BACKGROUND)

    center_x = 200
    center_y = 700
    origin = np.array([center_x, center_y])

    transformed_line = apply_transformation(LINE_COORDS, TRANSFORM_MATRIX)
    original_mid = calculate_midpoint(LINE_COORDS)
    transformed_mid = calculate_midpoint(transformed_line)

    draw_segment(screen, origin, COLOR_ORANGE, LINE_COORDS[0], LINE_COORDS[1])
    draw_segment(screen, origin, COLOR_DARK_BLUE, transformed_line[0], transformed_line[1])
    draw_segment(screen, origin, COLOR_LIGHT_GREEN, original_mid, transformed_mid, 3)

    draw_marker(screen, origin, COLOR_PINK, original_mid, 8)
    draw_marker(screen, origin, COLOR_PINK, transformed_mid, 8)

    render_text(screen, f"Original: ({LINE_COORDS[0][0]:.2f}, {LINE_COORDS[0][1]:.2f}) - ({LINE_COORDS[1][0]:.2f}, {LINE_COORDS[1][1]:.2f})", 20, 20)
    render_text(screen, f"Transformed: ({transformed_line[0][0]:.2f}, {transformed_line[0][1]:.2f}) - ({transformed_line[1][0]:.2f}, {transformed_line[1][1]:.2f})", 20, 60)

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
