import pygame
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
COLOR_WHITE = (245, 245, 245)  # Светло-серый
COLOR_BLACK = (50, 50, 50)  # Темно-серый
COLOR_RED = (200, 50, 50)  # Темно-красный
COLOR_GREEN = (50, 200, 50)  # Темно-зелёный
COLOR_BLUE = (50, 50, 200)  # Темно-синий
COLOR_ORANGE = (255, 165, 0)  # Оранжевый

TRANSFORMATION_MATRIX = np.array([[1, 2], [1, -3]])
LINE_COORDS = np.array([[-0.5, 1.5], [3, -2], [-1, -1], [3, 5 / 3]], dtype=float)

def apply_matrix_transformation(segment, matrix):
    reshaped_segment = segment.reshape(2, 2)
    transformed_segment = np.dot(reshaped_segment, matrix)
    return transformed_segment.reshape(2, 2)

def compute_line_slope(segment):
    x_start, y_start = segment[0]
    x_end, y_end = segment[1]
    if x_end - x_start == 0:
        return float('inf')
    return (y_end - y_start) / (x_end - x_start)

def render_line(surface, origin, color, start, end, thickness=3):
    x_start, y_start = int(start[0] + origin[0]), int(origin[1] - start[1])
    x_end, y_end = int(end[0] + origin[0]), int(origin[1] - end[1])
    pygame.draw.line(surface, color, (x_start, y_start), (x_end, y_end), thickness)

def render_text(surface, message, x, y, color=COLOR_BLACK, font_size=20):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(message, True, color)
    surface.blit(text_surface, (x, y))

def main():
    pygame.init()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Transformed Intersecting Lines")
    display.fill(COLOR_WHITE)

    origin_x = WINDOW_WIDTH / 2
    origin_y = WINDOW_HEIGHT / 2
    origin = np.array([origin_x, origin_y])

    scaling_factor = 80
    offset_x = 0
    offset_y = 0
    scaled_lines = LINE_COORDS * scaling_factor
    scaled_lines[:, 0] += offset_x
    scaled_lines[:, 1] += offset_y

    transformed_line1 = apply_matrix_transformation(scaled_lines[:2], TRANSFORMATION_MATRIX)
    transformed_line2 = apply_matrix_transformation(scaled_lines[2:], TRANSFORMATION_MATRIX)

    slope_original_line1 = compute_line_slope(scaled_lines[:2])
    slope_original_line2 = compute_line_slope(scaled_lines[2:])
    slope_transformed_line1 = compute_line_slope(transformed_line1)
    slope_transformed_line2 = compute_line_slope(transformed_line2)

    render_line(display, origin, COLOR_ORANGE, scaled_lines[0], scaled_lines[1])  # Изменено на оранжевый
    render_line(display, origin, COLOR_ORANGE, scaled_lines[2], scaled_lines[3])  # Изменено на оранжевый
    render_line(display, origin, COLOR_GREEN, transformed_line1[0], transformed_line1[1])  # Изменено на зелёный
    render_line(display, origin, COLOR_GREEN, transformed_line2[0], transformed_line2[1])  # Изменено на зелёный

    render_text(display, f"Initial Slope L1: {slope_original_line1:.2f}", 10, 10)
    render_text(display, f"Initial Slope L2: {slope_original_line2:.2f}", 10, 40)
    render_text(display, f"Transformed Slope L1: {slope_transformed_line1:.2f}", 10, 70)
    render_text(display, f"Transformed Slope L2: {slope_transformed_line2:.2f}", 10, 100)

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
